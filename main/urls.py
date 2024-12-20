from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from main.views import LessonScheduleViewSet \
   , StudyPlanViewSet, EduYearViewSet, AddEmployeeAPIView, LoginView, LogOutView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('schedules', LessonScheduleViewSet, basename='schedules')
router.register('plans', StudyPlanViewSet, basename='plans')
router.register('years', EduYearViewSet, basename='years')

urlpatterns = router.urls


schema_view = get_schema_view(
   openapi.Info(
      title="LSNSchedule API",
      default_version='v1',
      description="dars jadvalini avtomatik shakllantirish",
   )
)

urlpatterns += [
   path('add/employee/', AddEmployeeAPIView.as_view(), name='add-employee'),
   path('login/', LoginView.as_view(), name='login'),
   path('logout/', LogOutView.as_view(), name='logout'),
   path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]


