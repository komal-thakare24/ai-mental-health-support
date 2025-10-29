from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from matplotlib.style import context
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserRegisterSerializer
from .models import User
from django.http import JsonResponse
from ml_model.predict import predict_risk
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect


# ------------------- REST API REGISTER (for future React frontend) -------------------
class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ------------------- HTML FORM BASED VIEWS (for now) -------------------
@csrf_exempt
def signup_view(request):
    """Handles signup from modal (AJAX)"""
    if request.method == "POST":
        email = request.POST.get("email")
        username = request.POST.get("username") or email.split("@")[0]
        password = request.POST.get("password")

        if User.objects.filter(email=email).count() > 0:
            return JsonResponse({"success": False, "error": "Email already exists!"})

        user = User.objects.create_user(username=username, email=email, password=password)
    
        # Auto-login after signup
        login(request, user)

        return JsonResponse({
            "success": True,
            "username": username,
            "redirect_url": "/accounts/dashboard/"
        })

    return JsonResponse({"success": False, "error": "Invalid request method"})


@csrf_exempt
def login_view(request):
    """Handles login from modal (AJAX)"""
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                return JsonResponse({
                    "success": True,
                    "email": email,
                    "redirect_url": "/accounts/dashboard/"
                })
            return redirect("accounts:dashboard")
        else:
            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                return JsonResponse({"success": False, "error": "Invalid credentials!"})
            messages.error(request, "Invalid email or password")

    return render(request, "accounts/login.html")


@login_required
def dashboard(request):
    """Simple dashboard after login"""
    return render(request, "accounts/dashboard.html")


def logout_view(request):
    """Logout user"""
    logout(request)
    return redirect("home")  # redirects to home.html safely


def home(request):
   return render(request, "home.html")

@login_required
def profile_view(request):
    return render(request, "accounts/profile.html")


