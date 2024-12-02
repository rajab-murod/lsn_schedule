
import pytest
from rest_framework.authtoken.models import Token


@pytest.mark.django_db
def test_login(api_client, user):

   res = api_client.post('/api/login/', data={'username': user.username, 'password': user.password})
   assert res.status_code == 200
   # assert res.data['id'] == user.id
   # assert "token" in res.data  # The response should include the token
   # token = res.data["token"]
   # assert Token.objects.filter(key=token).exists()


