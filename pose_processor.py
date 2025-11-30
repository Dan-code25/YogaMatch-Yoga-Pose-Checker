import cv2
import time
import numpy as np
import mediapipe as mp
from collections import deque
from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtGui import QImage

from utils import extract_features

class VideoThread(QThread):
    # Connectors/updator to the main window
    change_pixmap_signal = pyqtSignal(QImage)
    update_status_signal = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.running = True
        self.session_active = False 
        self.current_model = None
        self.target_duration = 30.0
        self.show_landmarks = True 
        
        self.start_time = None
        self.elapsed_time = 0.0
        self.is_timing = False
        self.confidence_buffer = deque(maxlen=5)

    # Helper methods
    def set_model(self, model):
        self.current_model = model
        self.reset_session()

    def set_duration(self, duration):
        self.target_duration = duration
        
    def toggle_landmarks(self, enabled):
        self.show_landmarks = enabled
    
    def set_session_active(self, active):
        self.session_active = active
        if active:
            self.start_time = None
            self.elapsed_time = 0.0
            self.is_timing = False
            self.confidence_buffer.clear()

    def reset_session(self):
        self.elapsed_time = 0.0
        self.is_timing = False
        self.start_time = None
        self.confidence_buffer.clear()

    # Main processor method
    def run(self):
        cap = cv2.VideoCapture(0)
        mp_pose = mp.solutions.pose
        pose = mp_pose.Pose(
            static_image_mode=False, 
            model_complexity=1, 
            smooth_landmarks=True, 
            min_detection_confidence=0.5, 
            min_tracking_confidence=0.5
        )
        mp_drawing = mp.solutions.drawing_utils

        print("\n-- CAMERA STARTED --\n")

        while self.running:
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.flip(frame, 1)
            img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = pose.process(img_rgb)

            # Default Status
            status_msg = "Ready" if not self.session_active else "Waiting..."
            conf_str = "0%"
            is_correct = False
            time_str = "00:00.00"

            # Drawing landmarks
            if self.show_landmarks and results.pose_landmarks:
                mp_drawing.draw_landmarks(
                    frame, 
                    results.pose_landmarks, 
                    mp_pose.POSE_CONNECTIONS
                )

            # Status and confidence handler
            if self.session_active and self.current_model and results.pose_landmarks:
                try:
                    keypoints = extract_features(results.pose_landmarks.landmark, mp_pose)
                    prediction = self.current_model.predict([keypoints])[0]
                    confidence = self.current_model.predict_proba([keypoints])[0][1] * 100
                    
                    self.confidence_buffer.append(confidence)
                    avg_conf = np.mean(self.confidence_buffer)
                    conf_str = f"{avg_conf:.1f}%"

                    if prediction == 1 and avg_conf >= 80:
                        status_msg = "Correct Pose"
                        is_correct = True
                        
                        if not self.is_timing:
                            self.start_time = time.time()
                            self.is_timing = True
                        else:
                            self.elapsed_time += time.time() - self.start_time
                            self.start_time = time.time()
                    else:
                        status_msg = "Incorrect Pose"
                        self.is_timing = False 
                        self.start_time = None
                except Exception as e:
                    print(f"Prediction Error: {e}")

            # Timer Handler
            if self.session_active:
                remaining_seconds = max(0.0, self.target_duration - self.elapsed_time)
                if remaining_seconds == 0:
                    status_msg = "SESSION COMPLETED!"
                    is_correct = True
                
                mins, secs = divmod(int(remaining_seconds), 60)
                millis = int((remaining_seconds * 100) % 100)
                time_str = f"{mins:02}:{secs:02}.{millis:02}"
            else:
                mins, secs = divmod(int(self.target_duration), 60)
                time_str = f"{mins:02}:{secs:02}.00"

            # Status updator for the main window
            self.update_status_signal.emit({
                "status": status_msg,
                "confidence": conf_str,
                "time": time_str,
                "is_correct": is_correct
            })

            rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb_image.shape
            bytes_per_line = ch * w
            qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
            
            self.change_pixmap_signal.emit(qt_image)

        cap.release()

    def stop(self):
        self.running = False
        self.wait()