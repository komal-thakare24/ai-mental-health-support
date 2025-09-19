from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)   # email ko unique banate hain
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(
        max_length=10,
        choices=[("male", "Male"), ("female", "Female"), ("other", "Other")],
        null=True,
        blank=True,
    )

    USERNAME_FIELD = "email"   # login email se hoga
    REQUIRED_FIELDS = ["username"]   # username abhi bhi required rahega

    def __str__(self):
        return self.email
