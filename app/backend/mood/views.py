from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import MoodEntry
from django.utils import timezone

@login_required
def mood_tracker(request):
    if request.method == "POST":
        mood = request.POST.get("mood")
        activities = request.POST.get("activities", "")
        notes = request.POST.get("notes", "")

        MoodEntry.objects.create(
            user=request.user,
            mood=mood,
            activities=activities,
            notes=notes,
            date_logged=timezone.now()
        )
        return redirect("mood:view_progress")

    return render(request, "mood/mood_tracker.html")


@login_required
def mood_progress(request):
    return render(request, "mood_progress.html")