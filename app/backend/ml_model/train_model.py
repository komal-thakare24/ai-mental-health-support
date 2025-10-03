# ml_model/train_model.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, accuracy_score
import joblib
import os

# Path setup
DATA_PATH = "data/phq9data.xlsx"
MODEL_DIR = "ml_model/saved_model"
os.makedirs(MODEL_DIR, exist_ok=True)

print(f"Loading dataset from {os.path.abspath(DATA_PATH)} ...")
df = pd.read_excel(DATA_PATH)

print("Columns in dataset:", list(df.columns))

# Features (Q1..Q9)
feature_cols = [c for c in df.columns if c.upper().startswith("Q")]
X = df[feature_cols].values
print("Selected features:", feature_cols)

# Target: Risk_Level → make sure all are strings
df["Risk_Level"] = df["Risk_Level"].astype(str)
le = LabelEncoder()
y = le.fit_transform(df["Risk_Level"])

# Save label encoder
joblib.dump(le, os.path.join(MODEL_DIR, "label_encoder.joblib"))

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.15, random_state=42, stratify=y
)

# MLP Classifier
clf = MLPClassifier(hidden_layer_sizes=(32, 16), max_iter=500, random_state=42)
clf.fit(X_train, y_train)

# Evaluate
y_pred = clf.predict(X_test)
print("✅ Accuracy:", accuracy_score(y_test, y_pred))

# Safe classification report
report = classification_report(y_test, y_pred, target_names=le.classes_, zero_division=0)
print(report)

# Save model
joblib.dump(clf, os.path.join(MODEL_DIR, "phq9_mlp.joblib"))
print("📌 Model & label encoder saved to", MODEL_DIR)
