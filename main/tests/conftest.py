import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from main.models import EduYear, StudyPlan
from rest_framework.authtoken.models import Token


@pytest.fixture
def api_client():
   return APIClient()

@pytest.fixture
def year(db):
   year = EduYear.objects.create(title='2025-2026')
   return year

@pytest.fixture
def plan(db):
   plan = StudyPlan.objects.create(title='2025-2026')
   return plan

@pytest.fixture
def user(db):
   user = User.objects.create_user(username='testuser', password='securepassword')
   Token.objects.create(user=user)
   return user