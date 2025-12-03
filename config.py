import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_FOLDER = os.path.join(BASE_DIR, 'models')

# Trained Models
MODEL_FILES = {
  "Bow Pose" : "Bow Pose`.pkl",
  "Bridge Pose" : "bridge_pose.pkl",
  "Childs Pose": "childs_pose_detector.pkl",
  "Cobra Pose": "cobra_pose.pkl",
  "Dolphin Pose" : "Dolphin pose`.pkl",
  "Extended Puppy Pose" : "Extended_puppy_pose`.pkl",
  "Garland Pose" : "Garland Pose`.pkl",
  "Goddess Pose": "goddess_pose.pkl",
  "Hero Pose" : "Pose Hero`.pkl",
  "Inverted Lake Pose" : "Inverted Lake Pose`.pkl",
  "Sphinx Pose" : "sphinx_pose_detector.pkl",
  "Upward Salute Pose": "upward_salute_pose.pkl",
  "Warrior III Pose": "warrior_iii_pose_detector.pkl"
}

# Images for the guide
IMAGE_MAP = {
  "Bow Pose" : "images/Bow Pose PIc.png",
  "Bridge Pose" : "images/Bridge Pose.png",
  "Childs Pose": "images/child-pose.png",
  "Cobra Pose": "images/Cobra Pose.png",
  "Dolphin Pose" : "images/Dolphine Pose.png",
  "Extended Puppy Pose" : "images/Extended Pic.png",
  "Garland Pose" : "images/Garland Pic.png",
  "Goddess Pose": "images/Goddess Pose.png",
  "Hero Pose" : "images/Pose Hero Pic.png",
  "Inverted Lake Pose" : "images/Inverted Pic.png",
  "Sphinx Pose" : "images/Sphinx_Pose.png",
  "Upward Salute Pose": "images/Upward Salute.png",
  "Warrior III Pose": "images/Warrior_3.png"
}