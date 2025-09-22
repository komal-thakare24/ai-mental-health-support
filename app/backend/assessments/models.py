from django.db import models
from django.conf import settings

class Assessment(models.Model):
    TEST_CHOICES = (
        ('PHQ-9', 'PHQ-9'),
        ('GAD-7', 'GAD-7'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    assessment_type = models.CharField(max_length=20, choices=TEST_CHOICES)
    responses = models.JSONField()     # stores list/dict of answers
    score = models.IntegerField()
    risk_level = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} | {self.assessment_type} | {self.score}"
