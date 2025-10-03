# ml_model/predict.py
import os
import joblib
import numpy as np

# Paths
MODEL_DIR = os.path.join(os.path.dirname(__file__), "saved_model")
MODEL_PATH = os.path.join(os.path.dirname(__file__), "ml_model", "saved_model", "phq9_mlp.joblib")
ENCODER_PATH = os.path.join(os.path.dirname(__file__), "ml_model", "saved_model", "label_encoder.joblib")

# Load model and label encoder once (not every request)
clf = joblib.load(MODEL_PATH)
le = joblib.load(ENCODER_PATH)

def predict_risk(answers):
    """
    Predict depression risk level from PHQ-9 answers.
    
    Parameters:
        answers (list or array): List of 9 integers [Q1..Q9]
    
    Returns:
        dict: { "predicted_class": <string>, "confidence": <float> }
    """
    # Convert to numpy array and reshape (1 sample, 9 features)
    X = np.array(answers).reshape(1, -1)
    
    # Predict class index
    pred_idx = clf.predict(X)[0]
    pred_label = le.inverse_transform([pred_idx])[0]
    
    # Get probability (confidence)
    prob = clf.predict_proba(X).max()
    
    return {
        "predicted_class": str(pred_label),
        "confidence": float(round(prob, 3))
    }
