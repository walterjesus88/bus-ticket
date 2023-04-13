from django.test import TestCase, Client
from django.urls import reverse
from rest_framework.test import APIClient
from vehicles.models import Vehicle
from vehicles.views import VehicleViewSet
from vehicles.serializers import VehicleSerializer,VehicleModelSerializer,VehicleDetailSerializer
from rest_framework.test import APITestCase
from rest_framework import status
import json 
from collections import OrderedDict

class VehicleListViewTest(APITestCase):

	def setUp(self):
		self.url = '/api/vehicles/'
		self.model1 = Vehicle.objects.create(name='Model1')
		self.model2 = Vehicle.objects.create(name='Model2')
		self.serializer1 = VehicleSerializer(self.model1)
		self.serializer2 = VehicleSerializer(self.model2)

	def test_list(self):
		response = self.client.get(self.url, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		
		od2 = json.loads(json.dumps(response.data))		
		self.assertEqual(od2['results'], [self.serializer1.data, self.serializer2.data])

	def test_create(self):
		data = {'name': 'Model3','license': 'defss','available_seats' : 2,'description':'dddd'}
		response = self.client.post(self.url, data)
	
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		model = Vehicle.objects.get(name='Model3')
		serializer = VehicleSerializer(model)
		self.assertEqual(response.data, serializer.data)

	def test_retrieve(self):
		#url = self.client.get(self.url, args=[self.model1.id])
		#url = self.client.get(reverse('vehicle_detail', args=[self.model1.id]))
	
		url = f"{self.url}{self.model1.name}/"

		response = self.client.get(url)
		od2 = json.loads(json.dumps(response.data))	
		self.serializer1 = VehicleDetailSerializer(self.model1)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(od2, self.serializer1.data)


	def test_update(self):
		#url = reverse('mymodel-detail', args=[self.model1.id])
		url = f"{self.url}{self.model1.name}/"

		data = {'available_seats': 9}
		response = self.client.patch(url, data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		model = Vehicle.objects.get(id=self.model1.id)
		serializer = VehicleSerializer(model)
		od2 = json.loads(json.dumps(response.data))	
		self.assertEqual(od2, serializer.data)


	def test_destroy(self):
		#url = reverse('mymodel-detail', args=[self.model1.id])
		url = f"{self.url}{self.model1.name}/"
		response = self.client.delete(url)
		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
		self.assertFalse(Vehicle.objects.filter(name=self.model1.name).exists())

	def test_filter(self):
		url = f"{self.url}?name=Model1"
		response = self.client.get(url)
		print(response.status_code)
		self.assertEqual(response.status_code, status.HTTP_200_OK)