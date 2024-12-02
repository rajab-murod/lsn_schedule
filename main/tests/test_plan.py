def test_create_plan(api_client):
    payload = {

    }
    response = api_client.get('/api/plans/', data=payload, format='json')
    assert response.status_code == 201


def test_update_plan(api_client, plan):

   edit_payload = {
      "title": "2026-2027"
   }
   response = api_client.put(f'/api/plans/{plan.id}/', data=edit_payload, format='json')
   assert response.status_code == 200
   assert response.data['title'] == edit_payload['title']


def test_delete_plan(api_client, plan):
    res = api_client.delete(f'/api/plans/{plan.id}/')
    assert res.status_code == 204