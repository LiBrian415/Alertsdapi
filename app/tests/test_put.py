from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from django.urls import reverse
from ..models import Alert
from ..serializers import AlertSerializer, AlertUpdateSerializer

client = APIClient()

class PutAlertsTest(APITestCase):
    """ Test module for PUT alerts API """

    def setUp(self):
        self.alert1 = Alert.objects.create(
            title='Alert1',
            description='Description1',
            latitude=32.8801,
            longitude=117.2340
            )
        self.alert2 = Alert.objects.create(
            title='Alert2',
            description='Description2',
            latitude=47.569,
            longitude=-116.8920
            )
        self.valid_payload = {
            'description': 'New description'
        }
        self.invalid_payload = {
            'title': '',
            'latitude': 345.678901,
            'longitude': 12.345
        }

    def test_put_alert_valid(self):
        # get API response
        response = client.get(reverse('alert_specific', kwargs={'pk':
            self.alert1.pk}))
        alert = Alert.objects.get(pk=self.alert1.pk)
        serializer = AlertSerializer(alert)
        self.assertEqual(response.data, serializer.data)

        # put API response
        response = client.put(
                reverse('alert_specific', kwargs={'pk': self.alert1.pk}),
                self.valid_payload,
                format='json'
            )
        alert = Alert.objects.get(pk=self.alert1.pk)
        serializer = AlertSerializer(alert)
        self.assertEqual(response.data['description'], 'New description')
        self.assertEqual(response.data['description'],
        serializer.data['description'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_alert_invalid(self):
        # put API response
        response = client.put(
                reverse('alert_specific', kwargs={'pk': self.alert2.pk}),
                self.invalid_payload,
                format='json'
            )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

