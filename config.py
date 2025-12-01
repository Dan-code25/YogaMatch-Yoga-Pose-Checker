import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_FOLDER = os.path.join(BASE_DIR, 'models')

# Trained Models
MODEL_FILES = {
  "Boat Hero Pose" : "Boat Hero`.pkl",
  "Bow Pose" : "Bow Pose`.pkl",
  "Bridge Pose" : "bridge_pose.pkl",
  "Camel Pose" : "Camel Pose `.pkl",
  "Childs Pose": "childs_pose_detector.pkl",
  "Cobra Pose": "cobra_pose.pkl",
  "Cresent Moon Pose": "crescent_moon_pose_detector.pkl",
  "Dolphin Pose" : "Dolphin pose`.pkl",
  "Extended Puppy Pose" : "Extended_puppy_pose`.pkl",
  "Fierce Pose" : "Fierce Pose`.pkl",
  "Garland Pose" : "Garland Pose`.pkl",
  "Goddess Pose": "goddess_pose.pkl",
  "Hero Pose" : "Pose Hero`.pkl",
  "Heron Pose" : "Heron Pose`.pkl",
  "Inverted Lake Pose" : "Inverted Lake Pose`.pkl",
  "Sphinx Pose" : "sphinx_pose_detector.pkl",
  "Staff Pose" : "staff_pose_detector.pkl",
  "Tree Pose" : "tree_pose_detector.pkl",
  "Upward Salute Pose": "upward_salute_pose.pkl",
  "Warrior III Pose": "warrior_iii_pose_detector.pkl"
}

# Images for the guide
IMAGE_MAP = {
  "Boat Hero Pose" : "images/Boat Pose Pic.png",
  "Bow Pose" : "images/Bow Pose PIc.png",
  "Bridge Pose" : "images/Bridge Pose.png",
  "Camel Pose" : "images/Camel Pose PIc.png",
  "Childs Pose": "images/child-pose.png",
  "Cobra Pose": "images/Cobra Pose.png",
  "Cresent Moon Pose": "images/crescent_moon_pose.png",
  "Dolphin Pose" : "images/Dolphine Pose.png",
  "Extended Puppy Pose" : "images/Extended Pic.png",
  "Fierce Pose" : "images/Fierce Pose Pic.png",
  "Garland Pose" : "images/Garland Pic.png",
  "Goddess Pose": "images/Goddess Pose.png",
  "Hero Pose" : "images/Pose Hero Pic.png",
  "Heron Pose" : "images/Heron Pose Pic.png",
  "Inverted Lake Pose" : "images/Inverted Pic.png",
  "Sphinx Pose" : "images/Sphinx_Pose.png",
  "Staff Pose" : "images/staff_pose.png",
  "Tree Pose" : "images/tree_pose.png",
  "Upward Salute Pose": "images/Upward Salute.png",
  "Warrior III Pose": "images/Warrior_3.png"
}