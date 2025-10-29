from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Assessment
from .utils import calculate_phq9_score, calculate_gad7_score
import json


# 🧠 Assessment selection page
@login_required
def assessment_page(request):
    return render(request, "assessments.html")  # ✅ fixed path


# 🩺 PHQ-9 form and result logic
@login_required
def phq9_assessment(request):
    if request.method == "POST":
        responses = []
        for i in range(1, 10):  # q1 to q9
            try:
                responses.append(int(request.POST.get(f"q{i}", "0")))
            except ValueError:
                responses.append(0)

        total, level = calculate_phq9_score(responses)

        Assessment.objects.create(
            user=request.user,
            assessment_type="PHQ-9",
            responses=json.dumps(responses),
            score=total,
            risk_level=level,
        )

        return render(
            request,
            "result.html",  # ✅ using one common result page
            {"score": total, "severity": level, "test_name": "PHQ-9"}
        )

    return render(request, "assessments/phq9_form.html")

# 💭 GAD-7 form and result logic (for anxiety)
@login_required
def gad7_assessment(request):
    if request.method == "POST":
        responses = []
        for i in range(1, 8):  # q1 to q7
            try:
                responses.append(int(request.POST.get(f"q{i}", "0")))
            except ValueError:
                responses.append(0)

        total, level = calculate_gad7_score(responses)

        Assessment.objects.create(
            user=request.user,
            assessment_type="GAD-7",
            responses=json.dumps(responses),
            score=total,
            risk_level=level,
        )

        return render(
            request,
            "result.html",  # ✅ same result template
            {"score": total, "severity": level, "test_name": "GAD-7"}
        )

    return render(request, "assessments/gad7_form.html")

@login_required
def assessment_page(request):
    return render(request, "assessments/assessments.html")



