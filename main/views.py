from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from decouple import config

from main.serializers import LessonScheduleSerializer \
    , StudyPlanSerializer, EduYearSerializer
from main.models import LessonSchedule, StudyPlan, EduYear


class LessonScheduleViewSet(viewsets.ModelViewSet):
    queryset = LessonSchedule.objects.all()
    serializer_class = LessonScheduleSerializer


class HemisTokenAPIView(APIView):

    def get(self, request):
        return Response({'token': config('HEMIS_TOKEN')}, status=status.HTTP_200_OK)


class StudyPlanViewSet(viewsets.ModelViewSet):
    queryset = StudyPlan.objects.all()
    serializer_class = StudyPlanSerializer


class EduYearViewSet(viewsets.ModelViewSet):
    queryset = EduYear.objects.all()
    serializer_class = EduYearSerializer
