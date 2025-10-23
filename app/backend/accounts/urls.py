from django.urls import path
from . import views

app_name = "accounts"  # ✅ important for namespaced URLs

urlpatterns = [
    path("signup/", views.signup_view, name="signup"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("", views.home, name="home"),  # optional homepage
    path("phq9-result/", views.phq9_result, name="phq9_result"),
]
