from rest_framework import serializers
from main.models import LessonSchedule, StudyPlan, EduYear


class EduYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = EduYear
        fields = '__all__'


class StudyPlanSerializer(serializers.ModelSerializer):
    edu_year = EduYearSerializer(many=False)

    class Meta:
        model = StudyPlan
        fields = '__all__'


class LessonScheduleSerializer(serializers.ModelSerializer):
    study_plan = StudyPlanSerializer(many=False)
    class Meta:
        model = LessonSchedule
        fields = '__all__'
