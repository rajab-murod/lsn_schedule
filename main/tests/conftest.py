import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from main.models import EduYear


@pytest.fixture
def api_client():
   return APIClient()

@pytest.fixture
def year(db):
   year = EduYear.objects.create(title='2025-2026')
   return year

@pytest.fixture
def user(db):
   user = User.objects.create_user(username='testuser', password='testuser')
   return user