import numpy as np
import mediapipe as mp
import os
import joblib

# Data normalization function
def extract_features(landmarks, mp_pose):
    left_hip = landmarks[mp_pose.PoseLandmark.LEFT_HIP.value]
    right_hip = landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value]

    ref_x = (left_hip.x + right_hip.x) / 2
    ref_y = (left_hip.y + right_hip.y) / 2

    left_shoulder = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value]
    right_shoulder = landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value]
    
    body_scale = np.sqrt((left_shoulder.x - right_shoulder.x) ** 2 +
                         (left_shoulder.y - right_shoulder.y) ** 2)
    body_scale = max(body_scale, 1e-6)

    keypoints = []
    for lm in landmarks:
        norm_x = (lm.x - ref_x) / body_scale
        norm_y = (lm.y - ref_y) / body_scale
        keypoints.extend([norm_x, norm_y])
        
    return keypoints

# Model loader function
def load_all_models(model_files, model_folder):
    loaded_models = {}
    print("\n --- LOADING MODELS ---\n")
    i = 0
    for name, filename in model_files.items():
        path = os.path.join(model_folder, filename)
        i += 1
        if os.path.exists(path):
            try:
                loaded_models[name] = joblib.load(path)
                print(f"{i}. Loaded: {name}")
            except Exception as e:
                print(f"{i}. Error loading {name}: {e}")
        else:
            print(f"File not found: {path}")
    return loaded_models