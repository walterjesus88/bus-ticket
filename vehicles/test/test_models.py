from django.test import TestCase
from vehicles.models import Vehicle

class VehicleModelTestcase(TestCase):
	@classmethod
	def setUpTestData(cls):
		cls.vehicle=Vehicle.objects.create(name = "chosicano",license = "123gggg",available_seats =1)

	def test_string_method(self):
		vehicle = Vehicle.objects.get(id=1)
		expected_string =  vehicle.name
		self.assertEqual(str(vehicle), expected_string)	

	def test_update_vehicle(self):
		self.vehicle.name = "metropolitano"
		self.vehicle.license="A02"
		self.vehicle.save()

		updated_vehicle = Vehicle.objects.get(id=self.vehicle.id)
		self.assertEqual(updated_vehicle.name,"metropolitano")
		self.assertEqual(updated_vehicle.license,"A02")