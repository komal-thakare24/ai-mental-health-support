from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User

class User(AbstractUser):
    email = models.EmailField(unique=True)   # email ko unique banate hain
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(
        max_length=10,
        choices=[("male", "Male"), ("female", "Female"), ("other", "Other")],
        null=True,
        blank=True,
    )
class Profile(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
        ('prefer_not_to_say', 'Prefer not to say'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, blank=True)
    profession = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    # Health info
    has_therapist = models.CharField(max_length=5, blank=True)
    on_medication = models.CharField(max_length=5, blank=True)
    concerns = models.JSONField(default=list, blank=True, null=True)
    emergency_contact = models.CharField(max_length=100, blank=True)
    health_notes = models.TextField(blank=True)

    # Preferences
    email_notifications = models.BooleanField(default=True)
    mood_reminders = models.BooleanField(default=True)
    progress_reports = models.BooleanField(default=True)
    profile_visibility = models.BooleanField(default=False)
    data_sharing = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    
    USERNAME_FIELD = "email"   # login email se hoga
    REQUIRED_FIELDS = ["username"]   # username abhi bhi required rahega

    def __str__(self):
        return self.email
