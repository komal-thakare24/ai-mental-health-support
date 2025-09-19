# Architecture of AI-Enabled Mental Health Screening and Support System

## Overview
The AI-Enabled Mental Health Screening and Support System is designed to provide users with a comprehensive platform for mental health assessment and support. The system leverages Natural Language Processing (NLP) and predictive modeling to analyze user inputs and provide insights into mental health conditions.

## System Components

### 1. Data Collection
- **Raw Data**: Collected from various sources, including Google Forms, surveys, and other mental health assessment tools. This data is stored in the `data/raw` directory.
- **Processed Data**: After cleaning and preprocessing, the data is stored in the `data/processed` directory, ready for model training.

### 2. Machine Learning Model
- **Model Development**: The `ml-model/notebooks/model-development.ipynb` Jupyter notebook is used for exploratory data analysis, model selection, and evaluation. It includes visualizations to understand data distributions and model performance metrics.
- **Training**: The `ml-model/src/train.py` script handles the training of machine learning models using the processed data. It includes functions for data loading, preprocessing, and evaluation metrics.
- **Prediction**: The `ml-model/src/predict.py` script is responsible for making predictions based on user inputs. It utilizes the trained models to provide insights into mental health conditions.
- **Utilities**: The `ml-model/src/utils.py` file contains utility functions that assist in data preprocessing, model evaluation, and other common tasks.

### 3. Backend Application
- **Server**: The `app/backend/src/server.py` file initializes the backend server using Flask or Django, setting up middleware and routing for API requests.
- **API Routes**: The `app/backend/src/routes/screening.py` file defines the API endpoints for submitting mental health questionnaires and retrieving predictions based on user inputs.
- **User Model**: The `app/backend/src/models/user.py` file defines the user model, including properties for user data and methods for database interactions.

### 4. Frontend Application
- **Main Application**: The `app/frontend/src/App.tsx` file serves as the main entry point for the frontend application, managing routing and layout.
- **Screening Form**: The `app/frontend/src/components/ScreeningForm.tsx` file contains the React component for the mental health screening questionnaire, handling user input and submission.
- **Home Page**: The `app/frontend/src/pages/Home.tsx` file defines the home page layout, including navigation and links to other sections of the application.

## Interaction Flow
1. Users access the frontend application and fill out the mental health screening questionnaire.
2. The frontend sends the user input to the backend API.
3. The backend processes the input, interacts with the machine learning model to generate predictions, and returns the results to the frontend.
4. The frontend displays the results to the user, providing insights and recommendations based on the analysis.

## Conclusion
This architecture outlines the interaction between the various components of the AI-Enabled Mental Health Screening and Support System. By integrating data collection, machine learning, and a user-friendly interface, the system aims to enhance mental health assessment and support for users.