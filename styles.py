MAIN_STYLE = """
  QMainWindow {
    background-color: #121212;
  }

  QLabel {
    font-family: "Verdana", "Geneva", "sans-serif";
    color: #e0e0e0;
  }

  QLabel#header_title {
    font-size: 26px;
    font-weight: 800;
    letter-spacing: 1px;
  }

  QLabel[class="section_title"] {
    font-size: 14px;
    font-weight: 500;
    color: #a1a1aa;
    margin-bottom: 8px;
  }

  QFrame#sidebar {
    background-color: #18181b; /* Dark Zinc */
    border-right: 1px solid #27272a;
  }

  QFrame#box {
    background-color: #27272a; /* Card Background */
    border: 1px solid #3f3f46;
    border-radius: 12px;
    padding: 15px;
  }

  QLabel#video_label {
    background-color: #000000;
    border: 2px solid #3f3f46;
    border-radius: 16px;
    margin: 0px 80px;
  }

  QLabel#status_large {
      font-size: 32px;
      font-weight: 800;
      color: #00e676;
  }

  QLabel#time_large {
      font-size: 42px;
      font-weight: 700;
      color: #7830F7;
  }

"""

COMBO_STYLE = """
  QComboBox {
    border: 2px solid #585b70;
    padding: 3px 10px;
    min-height: 30px;
    background-color: #18181b;
    color: white;
    font-size: 14px;
  }

  QComboBox QAbstractItemView {
    background-color: #18181b;
    color: white;
    selection-background-color: #7830F7;
    border: 1px solid #585b70;
    outline: 0px;
  }

"""
SPIN_STYLE = """
  QSpinBox{
    background-color: #18181b;
    padding: 8px 30px 8px 10px;
    color: white;
    font-size: 16px;
    font-weight: bold;
  }
"""

RADIO_STYLE = """
  QRadioButton {
    color: #e0e0e0;
    font-size: 15px;
    font-weight: 700;
    padding: 5px;
  }

  QRadioButton::indicator {
    width: 16px;
    height: 16px;
    border: 2px solid #585b70;
  }

  QRadioButton::indicator:checked {
    background-color: #7830F7;
    border: 2px solid #4a169c;
  }

  QRadioButton::indicator:unchecked {
    background-color: transparent;
  }
"""

BUTTON_STYLE = """
  QPushButton {
    background-color: #7830F7; 
    color: white;
    border: none;
    border-radius: 10px;
    font-size: 18px;
    font-weight: 700;
    padding: 15px 20px;
    margin-bottom: 30px;
  }

  QPushButton:hover {
    background-color: #8b4bf9; 
    border: 1px solid #a77dfb;
  }

  QPushButton:pressed {
    background-color: #5b18d6; 
    padding-top: 18px;
    padding-bottom: 12px;
  }
"""

STOP_BUTTON_STYLE = """
  QPushButton {
    background-color:  #ef4444; 
    color: white;
    border: none;
    border-radius: 10px;
    font-size: 18px;
    font-weight: 700;
    padding: 15px 20px;
    margin-bottom: 30px;
  }
"""

