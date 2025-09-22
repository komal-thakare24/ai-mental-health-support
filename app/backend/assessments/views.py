from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Assessment
from .utils import calculate_phq9_score
import json

@login_required
def phq9_assessment(request):
    if request.method == "POST":
        # collect answers q1..q9
        responses = []
        for i in range(1, 10):
            val = request.POST.get(f"q{i}", "0")
            try:
              responses.append(int(val))
            except ValueError:
              responses.append(0)


        total, level = calculate_phq9_score("PHQ-9", responses)

        Assessment.objects.create(
            user=request.user,
            assessment_type="PHQ-9",
            responses=json.dumps(responses),
            score=total,
            risk_level=level,
        )

        return render(request, "assessments/phq9_result.html", {"score": total, "severity": level})

    return render(request, "assessments/phq9_form.html")
