# assessments/serializers.py
from rest_framework import serializers
from .models import Assessment
from .utils import calculate_phq9_score

class AssessmentSerializer(serializers.ModelSerializer):
    responses = serializers.ListField(
        child=serializers.IntegerField(min_value=0, max_value=3),
        allow_empty=False,
        write_only=True
    )
    score = serializers.IntegerField(read_only=True)
    risk_level = serializers.CharField(read_only=True)

    class Meta:
        model = Assessment
        fields = ["id", "user", "responses", "score", "risk_level", "created_at"]
        read_only_fields = ["id", "score", "risk_level", "created_at", "user"]

    def create(self, validated_data):
        responses = validated_data.pop("responses")
        total, level = calculate_phq9_score(responses)

        # save assessment
        assessment = Assessment.objects.create(
            user=self.context["request"].user,
            responses=responses,
            score=total,
            risk_level=level,
        )
        return assessment
