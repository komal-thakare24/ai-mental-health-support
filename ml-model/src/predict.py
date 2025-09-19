import joblib
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

class Predictor:
    def __init__(self, model_path, scaler_path):
        self.model = joblib.load(model_path)
        self.scaler = joblib.load(scaler_path)

    def preprocess_input(self, input_data):
        input_df = pd.DataFrame(input_data, index=[0])
        scaled_data = self.scaler.transform(input_df)
        return scaled_data

    def predict(self, input_data):
        processed_data = self.preprocess_input(input_data)
        prediction = self.model.predict(processed_data)
        return prediction

if __name__ == "__main__":
    model_path = 'path/to/your/model.pkl'  # Update with your model path
    scaler_path = 'path/to/your/scaler.pkl'  # Update with your scaler path
    predictor = Predictor(model_path, scaler_path)

    # Example input data
    input_data = {
        'feature1': value1,
        'feature2': value2,
        # Add all necessary features
    }

    prediction = predictor.predict(input_data)
    print("Prediction:", prediction)