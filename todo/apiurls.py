from django.db import router
from rest_framework.routers import DefaultRouter
from django.urls import path, include

from item.apis.viewsets import ItemViewset

router = DefaultRouter()
router.register("items", ItemViewset, basename="items")

urlpatterns = [
    path("", include(router.urls))
]
