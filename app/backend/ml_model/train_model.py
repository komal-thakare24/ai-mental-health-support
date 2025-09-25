# ml-model/train_model.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, accuracy_score
import joblib
import os

DATA_PATH = "ml-model/assessments_dataset.csv"
MODEL_DIR = "ml-model/saved_model"
os.makedirs(MODEL_DIR, exist_ok=True)

df = pd.read_csv(DATA_PATH)
# Features q1..q9 (for PHQ-9) - automatically select q1..q9 columns
feature_cols = [c for c in df.columns if c.startswith("q")]
X = df[feature_cols].values

# We convert risk_level to numeric classes
le = LabelEncoder()
y = le.fit_transform(df["risk_level"])

# Save label encoder so we can map back
joblib.dump(le, os.path.join(MODEL_DIR, "label_encoder.joblib"))

# train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=42, stratify=y)

# Simple MLP classifier
clf = MLPClassifier(hidden_layer_sizes=(32,16), max_iter=500, random_state=42)
clf.fit(X_train, y_train)

# Evaluate
y_pred = clf.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred, target_names=le.classes_))

# Save model
joblib.dump(clf, os.path.join(MODEL_DIR, "phq9_mlp.joblib"))
print("Model saved to", MODEL_DIR)
# To load the model and label encoder later:
# clf = joblib.load(os.path.join(MODEL_DIR, "phq9_mlp.joblib"))
# le = joblib.load(os.path.join(MODEL_DIR, "label_encoder.joblib"))
# predictions = clf.predict(new_data)
# predicted_labels = le.inverse_transform(predictions)
# predicted_probs = clf.predict_proba(new_data)
# predicted_probabilities = np.max(clf.predict_proba(new_data), axis=1)
