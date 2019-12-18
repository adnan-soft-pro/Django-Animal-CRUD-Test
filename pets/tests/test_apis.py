from faker import Faker
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from pets.models import Pet


class AnimalAPITest(TestCase):
    """ Test Animal apis """

    def setUp(self):
        fake = Faker()

        self.dummy_data1 = {
            'name': 'fake_dog',
            'type': 'DOG',
            'birthday': '2019-12-18'
        }
        self.dummy_data2 = {
            'name': 'fake_cat',
            'type': 'CAT',
            'birthday': '2019-12-18'
        }
        self.client = APIClient()
        self.fake_user = User.objects.create(
            email=fake.ascii_safe_email(),
            username=fake.user_name(),
            password=fake.password())
        self.client.force_login(self.fake_user)

    def test_create_animal(self):
        resp = self.client.post(
            '/api/create/', self.dummy_data1, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Pet.objects.count(), 1)
        self.assertEqual(Pet.objects.get().name, 'fake_dog')

    def test_list_animal(self):
        resp = self.client.post(
            '/api/create/', self.dummy_data1, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

        resp = self.client.get('/api/list/')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp.data.get('results')), 1)

    def test_update_animal(self):
        resp = self.client.post(
            '/api/create/', self.dummy_data1, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

        id = str(Pet.objects.get().id)
        resp = self.client.put(
            '/api/edit/{id}/'.format(id=id), self.dummy_data2, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data['type'], self.dummy_data2['type'])

    def test_delete_animal(self):
        resp = self.client.post(
            '/api/create/', self.dummy_data1, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

        id = str(Pet.objects.get().id)
        resp = self.client.delete('/api/edit/{id}/'.format(id=id))

        self.assertEqual(resp.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Pet.objects.count(), 0)
