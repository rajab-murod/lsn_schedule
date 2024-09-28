# import requests
# from decouple import config
# from main.models import Specialty, Group
#
#
# class HemisAPI:
#     def __init__(self):
#         self.headers = {
#             'Accept': 'application/json',
#             'Authorization': 'Bearer ' + config('HEMIS_TOKEN')
#         }
#         self.base_url = 'https://student.buxdu.uz/rest/v1/data/'
#
#     def get_specialties(self):
#         r = requests.get(self.base_url + 'specialty-list', headers=self.headers)
#         if r.status_code == 200:
#             pages = r.json()['data']['pagination']['pageCount']
#             for page in range(1, pages + 1):
#                 r = requests.get(self.base_url + 'specialty-list?page=' + str(page), headers=self.headers)
#                 if r.status_code == 200:
#                     items = r.json()['data']['items']
#                     specialty = []
#                     for item in items:
#                         specialty.append(Specialty(hemis_id=item['id'],
#                                               name=item['name'],
#                                               code=item['code'],
#                                               department=item['department'],
#                                               edu_type_code=item['educationType']['code'],
#                                               edu_type=item['educationType']['name'])
#                                          )
#                     Specialty.objects.bulk_create(specialty)
#                 else:
#                     return r.json()
#             return True
#         return r.json()
#
#     def get_all_group(self):
#         r = requests.get(self.base_url + 'group-list', headers=self.headers)
#         if r.status_code == 200:
#             pages = r.json()['data']['pagination']['pageCount']
#             for page in range(1, pages + 1):
#                 r = requests.get(self.base_url + 'group-list?page=' + str(page), headers=self.headers)
#                 if r.status_code == 200:
#                     items = r.json()['data']['items']
#                     group = []
#                     for item in items:
#                         print(item['id'])
#                         specialty = Specialty.objects.get(hemis_id=item['specialty']['id'])
#
#                         group.append(Group(hemis_id=item['id'],
#                                               name=item['name'],
#                                               specialty=specialty,
#                                               department=item['department']
#                                               )
#                                          )
#                     Group.objects.bulk_create(group)
#                 else:
#                     return r.json()
#             return True
#         return r.json()
#
