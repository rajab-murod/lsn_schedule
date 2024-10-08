from django.contrib.auth import logout, login
from rest_framework import filters, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from decouple import config

from main.hemis_api import HemisAPI
from main.serializers import LessonScheduleSerializer \
    , StudyPlanSerializer, EduYearSerializer, LoginSerializer
from main.models import LessonSchedule, StudyPlan, EduYear
from main.filters import StudyPlanFilter


class LessonScheduleViewSet(viewsets.ModelViewSet):
    queryset = LessonSchedule.objects.all()
    serializer_class = LessonScheduleSerializer


class StudyPlanViewSet(viewsets.ModelViewSet):
    queryset = StudyPlan.objects.all()
    serializer_class = StudyPlanSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = StudyPlanFilter


class EduYearViewSet(viewsets.ModelViewSet):
    queryset = EduYear.objects.all()
    serializer_class = EduYearSerializer


class AddEmployeeAPIView(APIView):
    def post(self, request):
        res = HemisAPI().get_employees()
        return Response({'result': res}, status=status.HTTP_200_OK)


class LoginView(APIView):

    def post(self, request):
        serializer = LoginSerializer(data=self.request.data,
                                     context={'request': self.request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        login(request, user)
        return Response({
            'id': user.id,
            'auth_token': token.key,
            'hemis_id': user.profile.hemis_id,
            'hemis_token': config('HEMIS_TOKEN'),
            'fio': f'{user.profile.last_name} {user.profile.first_name} {user.profile.surname}',
            'specialty': f'{user.profile.specialty}',
            'department_id': f'{user.profile.department_id}',
            'department_name': f'{user.profile.department_name}'

        }, status=status.HTTP_200_OK)


class LogOutView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, *args, **kwargs):
        token = Token.objects.get(user=self.request.user)
        token.delete()
        logout(self.request)
        return Response({'ok': True}, status=status.HTTP_200_OK)
