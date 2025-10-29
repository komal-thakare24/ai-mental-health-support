from django.db import models
from django.conf import settings

class MoodEntry(models.Model):
    MOOD_CHOICES = [
        ('happy', 'Happy'),
        ('calm', 'Calm'),
        ('sad', 'Sad'),
        ('anxious', 'Anxious'),
        ('stressed', 'Stressed'),
        ('neutral', 'Neutral'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    mood = models.CharField(max_length=20, choices=MOOD_CHOICES)
    activities = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    date_logged = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.mood} ({self.date_logged.date()})"
