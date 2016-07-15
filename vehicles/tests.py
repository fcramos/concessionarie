from django.test import TestCase
from vehicles.models import Manufacturer, Model, Vehicle


class ManufacturerTest(TestCase):
    def setUp(self):
        self.manufacturer = Manufacturer(
            name='Chevrolet'
        )
        self.manufacturer.save()

    def test_create(self):
        'Manufacture may be saved'
        self.assertEqual(1, self.manufacturer.pk)

    def test_str(self):
        'Manufacture string representation may be the name.'
        self.assertEqual('Chevrolet', str(self.manufacturer))


class ModelTest(TestCase):
    def setUp(self):
        self.manufacturer = Manufacturer(
            name='Chevrolet'
        )
        self.manufacturer.save()

        self.model = Model(
            name='Astra',
            manufacturer=self.manufacturer,
            type=Model.CAR_TYPE
        )
        self.model.save()

    def test_create(self):
        'Model instance may be saved.'
        self.assertEqual(1, self.model.pk)

    def test_str(self):
        'Model string representation may be the name.'
        self.assertEqual('Chevrolet Astra', str(self.model))


class VehicleTest(TestCase):
    def setUp(self):
        self.manufacturer = Manufacturer(
            name='Chevrolet'
        )
        self.manufacturer.save()

        self.model = Model(
            name='Astra',
            manufacturer=self.manufacturer,
            type=Model.CAR_TYPE
        )
        self.model.save()

        self.vehicle = Vehicle(
            model=self.model,
            color='Vermelho',
            mileage=104000,
            engine=2000
        )
        self.vehicle.save()

    def test_create(self):
        'Vehicle instance may be saved'
        self.assertEqual(1, self.vehicle.pk)

    def test_str(self):
        'Vehicle string representation may be the name.'
        self.assertEqual('Chevrolet Astra', str(self.vehicle))
