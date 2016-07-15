from rest_framework import viewsets

from vehicles.models import Manufacturer, Model, Vehicle
from vehicles.serializers import ManufacturerSerializer, ModelSerializer, VehicleSerializer


class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    search_fields = ('name', )


class ModelViewSet(viewsets.ModelViewSet):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer
    search_fields = ('name', 'manufacturer', 'type')


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    search_fields = ('model', 'color', 'mileage', 'engine')
