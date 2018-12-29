from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from django.urls import reverse
from ..models import Alert
from ..serializers import AlertSerializer, AlertUpdateSerializer

# initialize the APIClient app
client = APIClient()

class GetAlertsTest(APITestCase):
    """ Test module for GET alerts API """

    def setUp(self):
        self.alert1 = Alert.objects.create(
            title='Alert1',
            description='Description1',
            latitude=32.8801,
            longitude=117.2340,
            )
        self.alert2 = Alert.objects.create(
            title='Alert2',
            description='Description2',
            latitude=32.8801,
            longitude=-117.2340,
            )
        self.alert3 = Alert.objects.create(
            title='Alert3',
            description='Description3',
            latitude=132.8801,
            longitude=117.2340,
            )
        self.alert4 = Alert.objects.create(
            title='Alert4',
            description='Description4',
            latitude=-132.8801,
            longitude=17.2340,
            )

    def test_get_all_alerts(self):
        # get API response
        response = client.get(reverse('alert_list'))
        # get data from db
        alerts = Alert.objects.all()
        serializer = AlertSerializer(alerts, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_alert_valid(self):
        # get API response
        response = client.get(reverse('alert_specific', kwargs={'pk':
            self.alert2.pk}))
        # get data from db
        alert = Alert.objects.get(pk = self.alert2.pk)
        serializer = AlertSerializer(alert)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # get API response
        response = client.get(reverse('alert_specific', kwargs={'pk':
            self.alert3.pk}))
        #get data from db
        alert = Alert.objects.get(pk = self.alert3.pk)
        serializer = AlertSerializer(alert)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # get API response
        response = client.get(reverse('alert_specific', kwargs={'pk':
            self.alert1.pk}))
        # get data from db
        alert = Alert.objects.get(pk = self.alert1.pk)
        serializer = AlertSerializer(alert)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # get API response
        response = client.get(reverse('alert_specific', kwargs={'pk':
            self.alert4.pk}))
        # get data from db
        alert = Alert.objects.get(pk = self.alert4.pk)
        serializer = AlertSerializer(alert)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_alert_invalid(self):
        # get API response
        response = client.get(reverse('alert_specific', kwargs={'pk':30}))
        # get data from db
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        # get API response
        response = client.get(reverse('alert_specific', kwargs={'pk':100}))
        # get data from db
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)



