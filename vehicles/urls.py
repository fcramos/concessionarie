from django.conf.urls import url, include
from rest_framework import routers

from vehicles.views import ManufacturerViewSet

router = routers.DefaultRouter()
router.register(r'manufacturers', ManufacturerViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
]
