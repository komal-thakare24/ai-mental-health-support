from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserRegisterSerializer
from .models import User

# ------------------- REST API REGISTER (for future React frontend) -------------------
class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "User registered successfully!"},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ------------------- HTML FORM BASED VIEWS (for now) -------------------

def signup_view(request):
    """Signup form (HTML)"""
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
        else:
            user = User.objects.create_user(
                email=email,
                password=password,
                username=email   # 👈 email ko hi username bana do
            )
            messages.success(request, "Account created successfully. Please login.")
            return redirect("login")

    return render(request, "accounts/signup.html")



def login_view(request):
    """Login form (HTML)"""
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid email or password")

    return render(request, "accounts/login.html")


@login_required
def dashboard(request):
    """Simple dashboard after login"""
    return render(request, "accounts/dashboard.html")


def logout_view(request):
    """Logout user"""
    logout(request)
    return redirect("login")

def home(request):
    return render(request, "home.html")