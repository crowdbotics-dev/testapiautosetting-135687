from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors135687ViewSet

router = DefaultRouter()
router.register(
    "testconnectors135687", Testconnectors135687ViewSet, basename="testconnectors135687"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
