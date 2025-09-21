from django.urls import path
from . import views

urlpatterns = [
    path("phq9/", views.phq9_assessment, name="phq9"),
]