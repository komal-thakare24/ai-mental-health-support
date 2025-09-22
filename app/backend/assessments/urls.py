from django.urls import path
from . import views

app_name = "assessments"

urlpatterns = [
   path('phq9/', views.phq9_assessment, name='phq9_form'),
]
