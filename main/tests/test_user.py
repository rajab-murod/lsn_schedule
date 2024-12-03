import pytest
from rest_framework.authtoken.models import Token
import logging

logger = logging.getLogger(__name__)


def test_login(api_client, user):
   payload = {
      'username': user.username,
      'password': user.password
   }

   res = api_client.post('/api/login/', data=payload, format='json')
   logger.info("INFO:", res.data)
   assert res.status_code == 200
   # assert res.data['id'] == user.id
   assert "token" in res.data  # The response should include the token
   # token = res.data["token"]
   # assert Token.objects.filter(key=token).exists()


