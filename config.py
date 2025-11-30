import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_FOLDER = os.path.join(BASE_DIR, 'models')

# Trained Models
MODEL_FILES = {
  "Cobra Pose": "cobra_pose.pkl",
  "Childs Pose": "childs_pose_detector.pkl",
  "Cresent Moon Pose": "crescent_moon_pose_detector.pkl",
  "Downward Facing Tree Pose": "downward_facing_tree_pose_detector.pkl",
  "Flip the Dog Pose": "flip_the_dog_pose_detector.pkl",
  "Monkey Pose" : "monkey_pose_detector.pkl",
  "One Legged King Pigeon Pose" : "one_legged_king_pigeon_pose_detector.pkl",
  "Sphinx Pose" : "sphinx_pose_detector.pkl",

  "Staff Pose" : "staff_pose_detector.pkl",
  "Tree Pose" : "tree_pose_detector.pkl",
  "Goddess Pose": "goddess_pose.pkl",
  "Upward Salute Pose": "upward_salute_pose.pkl",
  "Bridge Pose" : "bridge_pose.pkl",
  "Plow Pose" : "plow_pose.pkl",
  "Seated Forward Fold Pose" : "Seated_foward_fold_pose.pkl",

  "Extended Puppy Pose" : "Extended_puppy_pose`.pkl",
  "Fierce Pose" : "Fierce Pose`.pkl",
  "Inverted Lake Pose" : "Inverted Lake Pose`.pkl",
  "Hero Pose" : "Pose Hero`.pkl",
  "Bow Pose" : "Bow Pose`.pkl",
  "Boat Hero Pose" : "Boat Hero`.pkl",
  "Camel Pose" : "Camel Pose `.pkl",
  "Extended Hand to Big Toe Pose": "Extended Hand to BigTOe`.pkl",
  "Garland Pose" : "Garland Pose`.pkl",
  "Dolphine Pose" : "Dolphine pose`.pkl",
  "Embryo Pose" : "Embryo pose`.pkl",
  "Heron Pose" : "Heron pose`.pkl",
  "Upward Facing Two Foot Pose" : "Upward Facing Two Foot  pose`.pkl",
}

# Images for the guide
IMAGE_MAP = {
  "Cobra Pose": "images/Cobra Pose.png",
  "Childs Pose": "images/child-pose.png",
  "Cresent Moon Pose": "images/crescent_moon_pose.png",
  "Downward Facing Tree Pose": "images/downward-facing-tree-pose.png",
  "Flip the Dog Pose": "images/flip-the-dog.png",
  "Monkey Pose" : "images/monkey_pose.png",
  "One Legged King Pigeon Pose" : "images/one-legged-king-pigeon-pose.png",
  "Sphinx Pose" : "images/Sphinx_Pose.png",
  
  "Staff Pose" : "images/staff_pose.png",
  "Tree Pose" : "images/tree_pose.png",
  "Goddess Pose": "images/Goddess Pose.png",
  "Upward Salute Pose": "images/Upward Salute.png",
  "Bridge Pose" : "images/Bridge Pose.png",
  "Plow Pose" : "images/Plow.png",
  "Seated Forward Fold Pose" : "images/Forward Fold.png",

  "Extended Puppy Pose" : "images/Extended Pic.png",
  "Fierce Pose" : "images/Fierce Pose Pic.png",
  "Inverted Lake Pose" : "images/Inverted Pic.png",
  "Hero Pose" : "images/Pose Hero Pic.png",#
  "Bow Pose" : "images/Bow Pose PIc.png",
  "Boat Hero Pose" : "images/Boat Pose Pic.png",
  "Camel Pose" : "images/Camel Pose PIc.png",
  "Extended Hand to Big Toe Pose": "images/Extended Hand To Bigtoe Pic.png",
  "Garland Pose" : "images/Garland Pic.png",
  "Dolphine Pose" : "images/Dolphine Pose.png",
  "Embryo Pose" : "images/Embro Pose PIc.png",
  "Heron Pose" : "images/Heron Pose Pic.png",
  "Upward Facing Two Foot Pose" : "images/Upward Foot PIc.png",
}