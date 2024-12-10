
def test_create_lesson(api_client, user, plan, year):
    payload = {
      "semester": "1",
      "date_time": "2024-12-10",
      "para": 1,
      "group": "1-1-PMI-23",
      "edu_year": year.id,
      "study_plan": plan.id,
      "owner": user.id
    }
    response = api_client.post('/api/schedules/', data=payload, format='json')
    assert response.status_code == 201


def test_fail_create_lesson(api_client):
    payload = {
      "semester": "2",
      "date_time": "2024-12-10",
      "para": 3,
      "group": "1-1-PMI-23"
    }
    response = api_client.post('/api/schedules/', data=payload, format='json')
    assert response.status_code == 400
    assert response.data["owner"] == ['This field is required.']
    assert response.data["edu_year"] == ['This field is required.']
    assert response.data["study_plan"] == ['This field is required.']


def test_detail_lesson(api_client, lesson, user, plan, year):
    response = api_client.get(f'/api/schedules/{lesson.id}/')
    assert response.status_code == 200
    assert response.data['id'] == lesson.id
    assert response.data['owner'] == user.id
    assert response.data['edu_year'] == year.id
    assert response.data['study_plan']['id'] == plan.id


def test_update_lesson(api_client, lesson):
    edit_payload = {
      "semester": "2",
      "date_time": "2024-12-20",
      "para": 4,
      "group": "1-1-PMI-20",
      "edu_year": 1,
      "study_plan": 1,
      "owner": 1
    }
    # check values before update
    assert '1' == lesson.semester
    assert '2024-12-10' == lesson.date_time
    assert 1 == lesson.para

    response = api_client.put(f'/api/schedules/{lesson.id}/', data=edit_payload, format='json')

    #check values after update
    assert response.status_code == 200
    assert response.data['group'] == edit_payload['group']
    assert response.data['para'] == edit_payload['para']
    assert response.data['date_time'] == edit_payload['date_time']


def test_delete_lesson(api_client, lesson):
    res = api_client.delete(f'/api/schedules/{lesson.id}/')
    assert res.status_code == 204
