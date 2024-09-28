from rest_framework import serializers
from main.models import LessonSchedule, StudyPlan, EduYear


class LessonScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonSchedule
        fields = '__all__'


class StudyPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyPlan
        fields = '__all__'


class EduYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = EduYear
        fields = '__all__'
