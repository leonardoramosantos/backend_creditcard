from django.urls import include
from django.urls import path
from rest_framework import routers

from card_manager.serializers import CreditCardViewSet

router = routers.DefaultRouter()
router.register(r'credit-card', CreditCardViewSet)

urlpatterns = [
    path('', include(router.urls))
]