from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Assessment

@login_required
def phq9_assessment(request):
    if request.method == "POST":
        # Get all 9 answers from form
        responses = []
        for i in range(1, 10):
            responses.append(int(request.POST.get(f"q{i}", 0)))

        # Calculate score
        total = sum(responses)
        # Risk level logic
        if total <= 4:
            level = "None"
        elif total <= 9:
            level = "Mild"
        elif total <= 14:
            level = "Moderate"
        elif total <= 19:
            level = "Moderately Severe"
        else:
            level = "Severe"

        # Save to DB
        Assessment.objects.create(
            user=request.user,
            assessment_type="PHQ-9",
            responses=responses,
            score=total,
            risk_level=level,
        )
        return render(request, "assessments/phq9_result.html", {"score": total, "risk": level})

    return render(request, "assessments/phq9_form.html")