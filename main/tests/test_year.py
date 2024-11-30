def test_detail_year(year, api_client):

   response = api_client.get(f'/api/years/{year.id}/')
   assert response.status_code == 200
   assert response.data['id'] == year.id
   assert response.data['title'] == year.title


def test_update_year(year, api_client):

   edit_payload = {
      "title": "2026-2027"
   }
   response = api_client.put(f'/api/years/{year.id}/', data=edit_payload, format='json')
   assert response.status_code == 200
   assert response.data['title'] == edit_payload['title']


def test_delete_year(year, api_client):

   res = api_client.delete(f'/api/years/{year.id}/')
   assert res.status_code == 204
