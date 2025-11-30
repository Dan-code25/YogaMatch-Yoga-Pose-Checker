import sys
import os
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel, 
                             QVBoxLayout, QHBoxLayout, QComboBox, QPushButton, 
                             QFrame, QSpinBox, QMessageBox, QRadioButton, QSizePolicy)
from PyQt6.QtCore import pyqtSlot, Qt, QUrl, QTimer
from PyQt6.QtGui import QPixmap, QImage, QIcon
from PyQt6.QtMultimedia import QSoundEffect

from styles import (MAIN_STYLE, COMBO_STYLE, SPIN_STYLE, RADIO_STYLE, 
                    BUTTON_STYLE, STOP_BUTTON_STYLE)
import config
from pose_processor import VideoThread
from utils import load_all_models

# Border styles
VIDEO_BASE_STYLE = "border-radius: 16px; background-color: #000000;"
STYLE_NEUTRAL = VIDEO_BASE_STYLE + "border: 2px solid #3f3f46;"
STYLE_SUCCESS = VIDEO_BASE_STYLE + "border: 4px solid #00e676;" 
STYLE_ERROR =   VIDEO_BASE_STYLE + "border: 4px solid #ef4444;"

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("YogaMatch")
    self.resize(1200, 800)
    icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images", "Logo.png")
    if os.path.exists(icon_path):
        self.setWindowIcon(QIcon(icon_path))    
    self.setStyleSheet(MAIN_STYLE)
    
    # Initialize camera thread
    self.thread = VideoThread()
    self.thread.change_pixmap_signal.connect(self.update_video_feed)
    self.thread.update_status_signal.connect(self.update_status)

    self.loaded_models = load_all_models(config.MODEL_FILES, config.MODEL_FOLDER)
    
    # Initialize sounds
    self.wrong_sound = QSoundEffect()
    self.sound_loop_active = False
    self.finish_sound = QSoundEffect()
    self.has_played_finish = False
    
    sound_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sounds', 'wrong.wav')
    if os.path.exists(sound_path):
        self.wrong_sound.setSource(QUrl.fromLocalFile(sound_path))
        self.wrong_sound.setVolume(1.0)
        self.wrong_sound.playingChanged.connect(self.on_sound_status_changed)

    finish_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sounds', 'complete.wav')
    if os.path.exists(finish_path):
        self.finish_sound.setSource(QUrl.fromLocalFile(finish_path))
        self.finish_sound.setVolume(1.0)
    else:
        print(f"Warning: Finish sound not found at {finish_path}")
    
    # Initialize the UI
    self.setup_ui()
    self.populate_models()
    self.thread.start()

  def setup_ui(self):
    central_widget = QWidget()
    self.setCentralWidget(central_widget)

    main_layout = QHBoxLayout(central_widget)
    main_layout.setContentsMargins(0, 0, 0, 0)
    main_layout.setSpacing(0)

    # SIDEBAR UI LAYOUT SETUP
    sidebar = QFrame()
    sidebar.setObjectName("sidebar")
    sidebar.setFixedWidth(500)

    sidebar_layout = QVBoxLayout(sidebar)
    sidebar_layout.setContentsMargins(20, 30, 20, 30)
    sidebar_layout.setSpacing(20)

    app_brand = QLabel("YogaMatch")
    app_brand.setObjectName("header_title")
    sidebar_layout.addWidget(app_brand)
    sidebar_layout.addSpacing(20)

    sidebar_layout.addWidget(self.style_label("SELECT POSE", "section_title"))

    self.model_combo = QComboBox()
    self.model_combo.addItem("Select a pose") 
    self.model_combo.setStyleSheet(COMBO_STYLE)
    self.model_combo.currentTextChanged.connect(self.update_guide_image)
    sidebar_layout.addWidget(self.model_combo)

    guide_box = QFrame()
    guide_box.setObjectName("box")
    guide_layout = QVBoxLayout(guide_box)

    self.guide_image = QLabel("No pose selected")
    self.guide_image.setAlignment(Qt.AlignmentFlag.AlignCenter)
    self.guide_image.setScaledContents(True)
    self.guide_image.setFixedHeight(400)
    self.guide_image.setStyleSheet("border: none;") 
   
    guide_layout.addWidget(self.guide_image)
    sidebar_layout.addWidget(guide_box)

    sidebar_layout.addWidget(self.style_label("TARGET DURATION", "section_title"))
    
    time_layout = QHBoxLayout()
    self.minute_spin = QSpinBox()
    self.minute_spin.setSuffix(" min")
    self.minute_spin.setRange(0, 59)
    self.minute_spin.setStyleSheet(SPIN_STYLE)

    self.second_spin = QSpinBox()
    self.second_spin.setSuffix(" sec")
    self.second_spin.setRange(0, 59)
    self.second_spin.setValue(30)
    self.second_spin.setStyleSheet(SPIN_STYLE)

    time_layout.addWidget(self.minute_spin)
    time_layout.addWidget(self.second_spin)
    sidebar_layout.addLayout(time_layout)

    sidebar_layout.addWidget(self.style_label("CAMERA SETTINGS", "section_title"))

    self.landmarks_radio = QRadioButton("Show Landmarks")
    self.landmarks_radio.setChecked(True)
    self.landmarks_radio.toggled.connect(self.toggle_landmarks)
    self.landmarks_radio.setStyleSheet(RADIO_STYLE)
    sidebar_layout.addWidget(self.landmarks_radio)
    sidebar_layout.addStretch()

    self.start_btn = QPushButton("Start Session")
    self.start_btn.setCursor(Qt.CursorShape.PointingHandCursor)
    self.start_btn.clicked.connect(self.toggle_session)
    self.start_btn.setStyleSheet(BUTTON_STYLE)
    sidebar_layout.addWidget(self.start_btn)

    main_layout.addWidget(sidebar)

    # CONTENT AREA LAYOUT SETUP
    content_area = QWidget()
    content_layout = QVBoxLayout(content_area)
    content_layout.setContentsMargins(10, 10, 10, 10) 
    content_layout.setSpacing(20)

    # header ui
    header_layout = QHBoxLayout()
    header_layout.addStretch()
    self.pose_title = QLabel("Ready for Session")
    self.pose_title.setStyleSheet("font-size: 28px; font-weight: bold; color: white;")
    self.pose_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
    header_layout.addWidget(self.pose_title)
    header_layout.addStretch()
    content_layout.addLayout(header_layout)

    # camera area ui
    self.video_label = QLabel()
    self.video_label.setObjectName("video_label")
    self.video_label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
    self.video_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    self.video_label.setMinimumSize(600, 500) 
    self.video_label.setStyleSheet(STYLE_NEUTRAL)

    content_layout.addWidget(self.video_label)

    # status ui
    stats_container = QHBoxLayout()
    stats_container.setSpacing(20)

    self.status_card = QFrame()
    self.status_card.setObjectName("box")
    status_layout = QVBoxLayout(self.status_card)
    status_layout.addWidget(self.style_label("STATUS", "section_title"))
    
    self.status_display = QLabel("Waiting...")
    self.status_display.setObjectName("status_large")
    self.status_display.setAlignment(Qt.AlignmentFlag.AlignCenter)
    status_layout.addWidget(self.status_display)
    stats_container.addWidget(self.status_card, 2)

    # timer ui
    timer_card = QFrame()
    timer_card.setObjectName("box")
    timer_layout = QVBoxLayout(timer_card)
    timer_layout.addWidget(self.style_label("TIMER", "section_title"))
    
    self.time_display = QLabel("00:00.00")
    self.time_display.setObjectName("time_large")
    self.time_display.setAlignment(Qt.AlignmentFlag.AlignCenter)
    timer_layout.addWidget(self.time_display)
    stats_container.addWidget(timer_card, 2)

    content_layout.addLayout(stats_container)
    main_layout.addWidget(content_area)

  def style_label(self, text, style_class):
    label = QLabel(text)
    label.setProperty("class", style_class)
    return label
  
  # Adds the loaded models to the combo box
  def populate_models(self):
      for name in self.loaded_models.keys():
          self.model_combo.addItem(name)

  @pyqtSlot(str)
  def update_guide_image(self, pose_name):
      if pose_name == "Select a pose":
          self.guide_image.setText("No pose selected")
          self.pose_title.setText("Ready for Session")
          self.thread.set_model(None)
          return

      self.pose_title.setText(f"Target: {pose_name}")
      img_path = config.IMAGE_MAP.get(pose_name)
      if img_path and os.path.exists(os.path.join(config.BASE_DIR, img_path)):
          full_path = os.path.join(config.BASE_DIR, img_path)
          pixmap = QPixmap(full_path)
          self.guide_image.setPixmap(pixmap.scaled(
              self.guide_image.size(), 
              Qt.AspectRatioMode.KeepAspectRatio, 
              Qt.TransformationMode.SmoothTransformation
          ))
      else:
          self.guide_image.setText("Image not found")
      
      model = self.loaded_models.get(pose_name)
      if model:
          self.thread.set_model(model)

  @pyqtSlot() # Session handler method
  def toggle_session(self):
      if self.thread.session_active:
          self.thread.set_session_active(False)
          self.start_btn.setText("Start Session")
          self.start_btn.setStyleSheet(BUTTON_STYLE)
          self.status_display.setText("Stopped")
          self.video_label.setStyleSheet(STYLE_NEUTRAL) 
          
          self.sound_loop_active = False
          if self.wrong_sound.isPlaying():
              self.wrong_sound.stop()
          
          self.model_combo.setEnabled(True)
          self.minute_spin.setEnabled(True)
          self.second_spin.setEnabled(True)
          
      else:
          if self.model_combo.currentText() == "Select a pose":
              QMessageBox.warning(self, "Warning", "Please select a pose first.")
              return

          total_seconds = (self.minute_spin.value() * 60) + self.second_spin.value()
          if total_seconds == 0:
             QMessageBox.warning(self, "Warning", "Please set a duration greater than 0.")
             return

          self.thread.set_duration(total_seconds)
          self.thread.set_session_active(True)
          
          self.has_played_finish = False
          
          self.start_btn.setText("Stop Session")
          self.start_btn.setStyleSheet(STOP_BUTTON_STYLE)
          
          self.model_combo.setEnabled(False)
          self.minute_spin.setEnabled(False)
          self.second_spin.setEnabled(False)


  @pyqtSlot(bool) # Show landmark handler method
  def toggle_landmarks(self, checked):
      self.thread.toggle_landmarks(checked)

  @pyqtSlot(QImage)
  def update_video_feed(self, qt_image):
      pixmap = QPixmap.fromImage(qt_image)
      scaled_pixmap = pixmap.scaled(
          self.video_label.size(), 
          Qt.AspectRatioMode.KeepAspectRatio, 
          Qt.TransformationMode.SmoothTransformation
      )
      self.video_label.setPixmap(scaled_pixmap)

  
  def on_sound_status_changed(self):
      if not self.wrong_sound.isPlaying() and self.sound_loop_active:
          QTimer.singleShot(500, self.play_next_loop)

  def play_next_loop(self):
      if self.sound_loop_active:
          self.wrong_sound.play()

  @pyqtSlot(dict)
  def update_status(self, data):
      self.status_display.setText(data["status"])
      self.time_display.setText(data["time"])

      if data["status"] == "SESSION COMPLETED!":
           self.status_display.setStyleSheet("font-size: 32px; font-weight: 800; color: #00e676;")
           self.video_label.setStyleSheet(STYLE_SUCCESS)
           
           # stops incorrect sound loop
           self.sound_loop_active = False
           if self.wrong_sound.isPlaying():
               self.wrong_sound.stop()
           
           # play session complete sound
           if not self.has_played_finish:
               self.finish_sound.play()
               self.has_played_finish = True
           
           return 
      
      self.has_played_finish = False

      # status handler
      if data["status"] == "Incorrect Pose" and self.thread.session_active:
           self.status_display.setStyleSheet("font-size: 32px; font-weight: 800; color: #ef4444;")
           self.video_label.setStyleSheet(STYLE_ERROR)
           if not self.sound_loop_active:
               self.sound_loop_active = True
               self.wrong_sound.play()

      elif data["is_correct"]:
          self.status_display.setStyleSheet("font-size: 32px; font-weight: 800; color: #00e676;")
          self.video_label.setStyleSheet(STYLE_SUCCESS)
          self.sound_loop_active = False
          if self.wrong_sound.isPlaying():
              self.wrong_sound.stop()

      else:
          self.status_display.setStyleSheet("font-size: 32px; font-weight: 800; color: #e0e0e0;")
          self.video_label.setStyleSheet(STYLE_NEUTRAL)
          self.sound_loop_active = False
          if self.wrong_sound.isPlaying():
              self.wrong_sound.stop()

  def closeEvent(self, event):
      self.thread.stop()
      event.accept()


if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = MainWindow()
  window.show()
  sys.exit(app.exec())