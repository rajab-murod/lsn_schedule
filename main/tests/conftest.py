import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from main.models import EduYear, StudyPlan, LessonSchedule
from rest_framework.authtoken.models import Token


@pytest.fixture
def api_client():
   return APIClient()


@pytest.fixture
def year(db):
   year = EduYear.objects.create(title='2025-2026')
   return year


@pytest.fixture
def user(db):
   user = User.objects.create_user(username='testuser', password='securepassword')
   Token.objects.create(user=user)
   return user


@pytest.fixture
def plan(db, year, user):
   plan = StudyPlan.objects.create(edu_year=year, subject_name='Matematika', teacher=user, hour=15)
   return plan


@pytest.fixture
def lesson(db, year, user, plan):
   lesson = LessonSchedule.objects.create(edu_year=year, study_plan=plan, owner=user, date_time='2024-12-10')
   return lesson
