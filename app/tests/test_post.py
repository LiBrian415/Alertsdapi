import json
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from django.urls import reverse
from ..models import Alert
from ..serializers import AlertSerializer, AlertUpdateSerializer

# initialize the APIClient app
client = APIClient()

class PostAlertsTest(APITestCase):
    """ Test module for POST alerts API"""

    def setUp(self):
        self.valid_payload1 = {
            'title': 'alert1',
            'description': 'description1',
            'latitude': 32.0018,
            'longitude': -118.0012
            }

        self.valid_payload2 = {
            'title': 'alert2',
            'description': 'description2',
            'latitude': 57.892,
            'longitude': 0
            }

        self.valid_payload3 = {
            'title': 'alert3',
            'description': '',
            'latitude': -112.0008,
            'longitude': 118
            }

        self.valid_payload4 = {
            'title': 'alert4',
            'description': 'description4',
            'latitude': -112.0008,
            'longitude': -160.0125
            }

        self.invalid_payload1 = {
            'description': '',
            'latitude': 45.05,
            'longitude': 27.348
            }

        self.invalid_payload2 = {
            'title': 'title',
            'description': '',
            }

        self.invalid_payload3 = {
            'title': 'title',
            'description': '',
            'latitude': 13.444567,
            'longitude': 123.12345
            }

    def test_create_valid_alerts(self):
        # post API
        response = client.post(
            reverse('alert_list'),
            self.valid_payload1,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # post API
        response = client.post(
            reverse('alert_list'),
            self.valid_payload2,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # post API
        response = client.post(
            reverse('alert_list'),
            self.valid_payload3,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # post API
        response = client.post(
            reverse('alert_list'),
            self.valid_payload4,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_alert(self):
        # post API
        response = client.post(
            reverse('alert_list'),
            self.invalid_payload1,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # post API
        response = client.post(
            reverse('alert_list'),
            self.invalid_payload2,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # post API
        response = client.post(
            reverse('alert_list'),
            self.invalid_payload3,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

