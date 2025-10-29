from django.urls import path
from . import views

app_name = "mood"

urlpatterns = [
    path('', views.mood_tracker, name='mood_tracker'),
    path('progress/', views.mood_progress, name='progress'),

]
