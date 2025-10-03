from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserRegisterSerializer
from .models import User
from django.shortcuts import render
from django.http import JsonResponse
from ml_model.predict import predict_risk   # import our function
import json

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

def phq9_result(request):
    if request.method == "POST":
        try:
            # Collect answers from POST form
            answers = [
                int(request.POST.get("Q1")),
                int(request.POST.get("Q2")),
                int(request.POST.get("Q3")),
                int(request.POST.get("Q4")),
                int(request.POST.get("Q5")),
                int(request.POST.get("Q6")),
                int(request.POST.get("Q7")),
                int(request.POST.get("Q8")),
                int(request.POST.get("Q9")),
            ]
            
            # Call ML model
            result = predict_risk(answers)
            
            # Render result page
            return render(request, "accounts/phq9_result.html", {
                "prediction": result["predicted_class"],
                "confidence": result["confidence"]
            })
        
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    
    # If GET request, just return empty page
    return render(request, "accounts/phq9_form.html")