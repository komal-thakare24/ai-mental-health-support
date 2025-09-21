from django.db import models
from django.conf import settings

class Assessment(models.Model):
    # Link to the user who took the test
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # Type of assessment
    assessment_type = models.CharField(max_length=20, choices=[('PHQ-9', 'PHQ-9'), ('GAD-7', 'GAD-7')])

    # Store answers as JSON (list of responses)
    responses = models.JSONField()

    # Calculated score
    score = models.IntegerField()

    # Risk level (None, Mild, Moderate, Severe)
    risk_level = models.CharField(max_length=20)

    # Timestamp
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.assessment_type} - {self.score}"
