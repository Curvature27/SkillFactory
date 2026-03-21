from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from mount.models import Pereval, Users, Coords, Level
from mount.serializers import PerevalSerializer


# pip install coverage
# coverage run --source='.' manage.py test .
# coverage report
# coverage html


class PerevalApiTestCase(APITestCase):
    def setUp(self):
        self.pereval_1 = Pereval.objects.create(
            beauty_title='Beauty title 1',
            title='Title 1',
            other_titles='Other titles 1',
            connect='',
            add_time='22-05-2024 19:44:13',
            tourist_id=Users.objects.create(
                email='user1@mail.ru',
                last_name='lastname1',
                first_name='firstname1',
                patronymic='patronymic1',
                phone='+11111111111'
            ),
            coord_id=Coords.objects.create(
                latitude='11.11111',
                longitude='22.22222',
                height='1111'
            ),
            level=Level.objects.create(
                winter_lev='1A',
                spring_lev='1A',
                summer_lev='1A',
                autumn_lev='1A'
            ),
            status='NW'
        )

        self.pereval_2 = Pereval.objects.create(
            beauty_title='Beauty title 2',
            title='Title 2',
            other_titles='Other titles 2',
            connect='',
            add_time='23-05-2024 16:13:36',
            tourist_id=Users.objects.create(
                email='user2@mail.ru',
                last_name='lastname2',
                first_name='firstname2',
                patronymic='partonymic2',
                phone='+22222222222'
            ),
            coord_id=Coords.objects.create(
                latitude='33.33333',
                longitude='44.44444',
                height='2222'
            ),
            level=Level.objects.create(
                winter_lev='',
                spring_lev='1A',
                summer_lev='1A',
                autumn_lev='1A'
            ),
            status='NW'
        )

    def test_get(self):
        url = reverse('perevals-list')
        resource = self.client.get(url)
        serializer_data = PerevalSerializer([self.pereval_1, self.pereval_2], many=True).data
        # print('---------------------------------------')
        # print(serializer_data)
        # print('---------------------------------------')
        # print(resource.data)
        # print('---------------------------------------')

        # сравнивает serializer_data и resource.data
        self.assertEqual(serializer_data, resource.data['results'])
        # проверяет, что количество serializer_data = 2
        self.assertEqual(len(serializer_data), 2)
        self.assertEqual(status.HTTP_200_OK, resource.status_code)


class PrevalSerializerTestCase(TestCase):
    def setUp(self):
        self.pereval_1 = Pereval.objects.create(
            beauty_title='Beauty title 1',
            title='Title 1',
            other_titles='Other titles 1',
            connect='',
            add_time='22-05-2024 19:44:13',
            tourist_id=Users.objects.create(
                email='user1@mail.ru',
                last_name='lastname1',
                first_name='firstname1',
                patronymic='patronymic1',
                phone='+11111111111'
            ),
            coord_id=Coords.objects.create(
                latitude='11.11111',
                longitude='22.22222',
                height=1111
            ),
            level=Level.objects.create(
                winter_lev='1A',
                spring_lev='1A',
                summer_lev='1A',
                autumn_lev='1A'
            ),
            status='NW'
        )

        self.pereval_2 = Pereval.objects.create(
            beauty_title='Beauty title 2',
            title='Title 2',
            other_titles='Other titles 2',
            connect='',
            add_time='22-05-2024 19:44:13',
            tourist_id=Users.objects.create(
                email='user2@mail.ru',
                last_name='lastname2',
                first_name='firstname2',
                patronymic='patronymic2',
                phone='+22222222222'
            ),
            coord_id=Coords.objects.create(
                latitude='33.33333',
                longitude='44.44444',
                height=2222
            ),
            level=Level.objects.create(
                winter_lev='',
                spring_lev='1A',
                summer_lev='1A',
                autumn_lev='1A'
            ),
            status='NW'
        )

    def test_check(self):
        serializer_data = PerevalSerializer([self.pereval_1, self.pereval_2], many=True).data
        expected_data = [
            {
                "beauty_title": "Beauty title 1",
                "title": "Title 1",
                "other_titles": "Other titles 1",
                "connect": "",
                'add_time': self.pereval_1.add_time.strftime('%d-%m-%Y %H:%M:%S'),
                "tourist_id": {
                    "email": "user1@mail.ru",
                    "last_name": "lastname1",
                    "first_name": "firstname1",
                    "patronymic": "patronymic1",
                    "phone": "+11111111111"
                },
                "coord_id": {
                    "latitude": "11.11111000",
                    "longitude": "22.22222000",
                    "height": 1111
                },
                "level": {
                    "winter": "4A",
                    "spring": "2A",
                    "summer": "1A",
                    "autumn": "3A"
                },
                'images': [],
                'status': 'NW'
            },
            {
                'beauty_title': 'Beauty title 2',
                'title': 'Title 2',
                'other_titles': 'Other titles 2',
                'connect': '',
                'add_time': self.pereval_2.add_time.strftime('%d-%m-%Y %H:%M:%S'),
                'tourist_id': {
                    'email': 'user2@mail.ru',
                    'last_name': 'lastname2',
                    'first_name': 'firstname2',
                    'patronymic': 'patronymic2',
                    'phone': '+22222222222'
                },
                'coord_id': {
                    'latitude': '33.33333000',
                    'longitude': '44.44444000',
                    'height': 2222
                },
                'level': {
                    'winter': '4A',
                    'spring': '2A',
                    'summer': '1A',
                    'autumn': '3A'
                },
                'images': [],
                'status': 'NW'
            }
        ]

        # print("-------------------")
        # print(serializer_data)
        # print("-------------------")
        # print(expected_data)
        # print("-------------------")
        self.assertEqual(serializer_data, expected_data)

# python manage.py test .
