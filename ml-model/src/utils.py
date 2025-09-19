def load_data(file_path):
    # Function to load data from a specified file path
    import pandas as pd
    return pd.read_csv(file_path)

def preprocess_data(data):
    # Function to preprocess the data
    # This can include handling missing values, encoding categorical variables, etc.
    data = data.dropna()  # Example: dropping missing values
    return data

def evaluate_model(model, X_test, y_test):
    # Function to evaluate the model performance
    from sklearn.metrics import accuracy_score, classification_report
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    report = classification_report(y_test, predictions)
    return accuracy, report

def save_model(model, file_path):
    # Function to save the trained model to a file
    import joblib
    joblib.dump(model, file_path)

def load_model(file_path):
    # Function to load a trained model from a file
    import joblib
    return joblib.load(file_path)