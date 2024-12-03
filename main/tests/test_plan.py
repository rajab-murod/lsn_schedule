def test_create_plan(api_client, user, year):
    payload = {
          "edu_year": {
            "id":year.id,
                "title": year.title,
              },
          "semester": "1",
          "edu_type": "M",
          "subject_name": "Subject1",
          "hour": 12,
          "groups": "string",
          "group_division": True,
          "thread": True,
          "confirm": True,
          "teacher": user.id
    }
    response = api_client.post('/api/plans/', data=payload, format='json')
    assert response.status_code == 201


def test_update_plan(api_client, plan):

   edit_payload = {
      "subject_name": "Fizika",
       "hour":30
   }
   response = api_client.patch(f'/api/plans/{plan.id}/', data=edit_payload, format='json')
   assert response.status_code == 200
   assert response.data['subject_name'] == edit_payload['subject_name']


def test_delete_plan(api_client, plan):
    res = api_client.delete(f'/api/plans/{plan.id}/')
    assert res.status_code == 204