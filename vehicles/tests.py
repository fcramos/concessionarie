from django.test import TestCase
from vehicles.models import Manufacturer


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
