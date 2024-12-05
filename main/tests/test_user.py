import pytest
from rest_framework.authtoken.models import Token


@pytest.mark.django_db
def test_login(api_client, user):
   payload = {
      'username': "testuser",
      'password': "securepassword",
   }

   res = api_client.post('/api/login/', data=payload, format='json')
   assert res.status_code == 200
   assert res.data['id'] == user.id
   assert "auth_token" in res.data
   token = res.data["auth_token"]
   assert Token.objects.filter(key=token).exists()


