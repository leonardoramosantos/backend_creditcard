from rest_framework import serializers
from rest_framework import viewsets

from .models import CreditCard

class CreditCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditCard
        fields = ["id", "exp_date", "holder", "card_number", "cvv", "brand"]


class CreditCardViewSet(viewsets.ModelViewSet):
    queryset = CreditCard.objects.all()
    serializer_class = CreditCardSerializer