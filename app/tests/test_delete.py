from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from django.urls import reverse
from ..models import Alert
from ..serializers import AlertSerializer, AlertUpdateSerializer

client = APIClient()

class DeleteAlertTest(APITestCase):
    """ Test module for DELETE alerts API """

    def setUp(self):
        self.alert1 = Alert.objects.create(
            title='Alert1',
            description='',
            latitude=32,
            longitude=107
            )
        self.alert2 = Alert.objects.create(
            title='Alert2',
            description='Description2',
            latitude=-45,
            longitude=379
            )

    def test_delete_alert_valid(self):
        # delete API response
        response = client.delete(
            reverse('alert_specific', kwargs={'pk': self.alert1.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_alert_invalid(self):
        # invalid delete API response
        response = client.delete(
            reverse('alert_specific', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
