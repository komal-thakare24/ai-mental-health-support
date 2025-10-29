from django.urls import path
from . import views

app_name = "assessments"

urlpatterns = [
    path('', views.assessment_page, name='assessment_page'),
    path('phq9/', views.phq9_assessment, name='phq9_assessment'),
    path('gad7/', views.gad7_assessment, name='gad7_assessment'),
]
