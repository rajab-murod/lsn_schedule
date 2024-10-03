import requests
from decouple import config
from django.contrib.auth.models import User
from main.models import Profile


class HemisAPI:
    def __init__(self):
        self.headers = {
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + config('HEMIS_TOKEN')
        }
        self.base_url = 'https://student.buxdu.uz/rest/v1/data/'

    def get_employees(self):
        r = requests.get(self.base_url + 'employee-list?type=all&_employee_type=12&limit=100', headers=self.headers)
        if r.status_code == 200:
            pages = r.json()['data']['pagination']['pageCount']
            for page in range(1, pages + 1):
                r = requests.get(self.base_url + 'employee-list?type=all&_employee_type=12&limit=100&page=' + str(page), headers=self.headers)
                if r.status_code == 200:
                    items = r.json()['data']['items']
                    # users = []
                    # profiles = []
                    for item in items:
                        user = User.objects.create_user(username=item['employee_id_number'], password=item['employee_id_number'])
                        profile = Profile.objects.create(user=user,
                                          hemis_id=item['id'],
                                          first_name=item['first_name'],
                                          last_name=item['second_name'],
                                          surname=item['third_name'],
                                          specialty=item['specialty'],
                                          department_id=item['department']['id'],
                                          department_name=item['department']['name']
                                          )
                        print(user.username)
                        # users.append(user)
                        # profiles.append(profile)
                    # User.objects.bulk_create(users)
                    # Profile.objects.bulk_create(profiles)
                else:
                    return r.json()
            return True
        return r.json()


