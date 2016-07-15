from django.conf.urls import url, include
from rest_framework import routers

from vehicles.views import ManufacturerViewSet, ModelViewSet

router = routers.DefaultRouter()
router.register(r'manufacturers', ManufacturerViewSet)
router.register(r'models', ModelViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
]
