from django.contrib.auth import authenticate
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


    def create(self, validated_data):
        edu_year_data = validated_data.pop('edu_year')
        edu_year, _ = EduYear.objects.get_or_create(**edu_year_data)
        plan = StudyPlan.objects.create(**validated_data, edu_year=edu_year)
        return plan


class ReadyOnlyLessonScheduleSerializer(serializers.ModelSerializer):
    study_plan = StudyPlanSerializer(many=False)

    class Meta:
        model = LessonSchedule
        fields = '__all__'


class LessonScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonSchedule
        fields = '__all__'


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
        else:
            msg = '"username" va "password" kiritilishi majburiy!'
            raise serializers.ValidationError(msg, code='authorization')
        attrs['user'] = user
        return attrs
