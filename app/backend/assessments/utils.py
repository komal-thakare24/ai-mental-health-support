def calculate_score(assessment_type, responses):
    """
    Calculate total score and risk level for PHQ-9 / GAD-7
    responses: list of integers (0–3 for each question)
    """

    score = sum(responses)

    risk_level = "None"

    if assessment_type == "PHQ-9":
        if score <= 4:
            risk_level = "None"
        elif score <= 9:
            risk_level = "Mild"
        elif score <= 14:
            risk_level = "Moderate"
        elif score <= 19:
            risk_level = "Moderately Severe"
        else:
            risk_level = "Severe"

    elif assessment_type == "GAD-7":
        if score <= 4:
            risk_level = "None"
        elif score <= 9:
            risk_level = "Mild"
        elif score <= 14:
            risk_level = "Moderate"
        else:
            risk_level = "Severe"

    return score, risk_level
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = "accounts.User"
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],

}
