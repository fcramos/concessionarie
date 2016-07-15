from django.conf.urls import url, include
from rest_framework import routers

from vehicles.views import ManufacturerViewSet, ModelViewSet, VehicleViewSet

router = routers.DefaultRouter()
router.register(r'manufacturers', ManufacturerViewSet)
router.register(r'models', ModelViewSet)
router.register(r'vehicles', VehicleViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
]
