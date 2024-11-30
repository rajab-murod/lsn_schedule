def test_login(api_client, user):
   res = api_client.post('/api/login/', data={'username': user.username, 'password': user.password})
   assert res.status_code == 200
   assert res.data['id'] == user.id