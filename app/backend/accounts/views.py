from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserRegisterSerializer
from .models import User
from django.http import JsonResponse
from ml_model.predict import predict_risk
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


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
@csrf_exempt
def signup_view(request):
    """Handles signup from modal (AJAX)"""
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(email=email).exists():
            return JsonResponse({"success": False, "error": "Email already exists!"})

        user = User.objects.create_user(
            username=email,
            email=email,
            password=password
        )

        # Auto-login after signup
        login(request, user)

        return JsonResponse({
            "success": True,
            "message": "Account created successfully!",
            "redirect_url": "/accounts/dashboard/"
        })

    return JsonResponse({"success": False, "error": "Invalid request method"})

@csrf_exempt
def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            # return JSON if AJAX request
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({"success": True, "email": email, "redirect_url": "/accounts/dashboard/"})
            return redirect("accounts:dashboard")
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({"success": False, "error": "Invalid credentials"})
            messages.error(request, "Invalid email or password")

    return JsonResponse({"success": True, "email": email, "redirect_url": "/dashboard/"})

 
@login_required
def dashboard(request):
    """Simple dashboard after login"""
    return render(request, "accounts/dashboard.html")


def logout_view(request):
    """Logout user"""
    logout(request)
    return redirect("accounts:login")  # ✅ namespace added


def home(request):
    return render(request, "home.html")


def phq9_result(request):
    if request.method == "POST":
        try:
            answers = [
                int(request.POST.get(f"Q{i}")) for i in range(1, 10)
            ]
            
            result = predict_risk(answers)
            
            return render(request, "accounts/phq9_result.html", {
                "prediction": result["predicted_class"],
                "confidence": result["confidence"]
            })
        
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    
    return render(request, "accounts/phq9_form.html")
