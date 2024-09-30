from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
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


class StudyPlanAPIView(APIView):
    def get(self, request, *args, **kwargs):
        g_name = request.query_params.get('name')
        qs = StudyPlan.objects.filter(groups__icontains=g_name).values()
        return Response({'data': qs}, status=status.HTTP_200_OK)


class StudyPlanViewSet(viewsets.ModelViewSet):
    queryset = StudyPlan.objects.all()
    serializer_class = StudyPlanSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['edu_year_id', 'semester', 'edu_type', 'teacher_id', 'confirm']
    search_fields = ['^groups__name']

    # def list(self, request, *args, **kwargs):
    #     g_name = request.query_params.get('gname')
    #     if g_name is not None:
    #         qs = StudyPlan.objects.filter(groups__icontains=g_name).values()
    #         return Response({'data': qs}, status=status.HTTP_200_OK)
    #     qs = StudyPlan.objects.all().values()
    #     return Response({'data': qs}, status=status.HTTP_200_OK)


class EduYearViewSet(viewsets.ModelViewSet):
    queryset = EduYear.objects.all()
    serializer_class = EduYearSerializer
