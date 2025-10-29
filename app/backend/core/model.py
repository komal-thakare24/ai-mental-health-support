from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

# ---- UserProfile: extra info for each User ----
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    gender = models.CharField(
        max_length=10,
        choices=(('M', 'Male'), ('F', 'Female'), ('O', 'Other')),
        blank=True
    )
    dob = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return getattr(self.user, 'username', str(self.user))

# ---- Assessment: store each PHQ-9 / GAD-7 test ----
class Assessment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assessments')
    questionnaire_type = models.CharField(
        max_length=20,
        choices=(('PHQ-9', 'PHQ-9'), ('GAD-7', 'GAD-7'))
    )
    responses = models.JSONField()        # answers as JSON (needs Django 3.1+)
    total_score = models.IntegerField()
    risk_level = models.CharField(max_length=30)  # e.g., Mild, Moderate
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.questionnaire_type} - {self.total_score}"