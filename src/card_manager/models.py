from django.db import models

from creditcard import CreditCard as CCModule

from .custom_fields import CustomEncryptedField
from .custom_fields import CustomDateGeneratedField
from .functions import get_last_day_of_month_date
from .validations import validate_exp_date
from .validations import validate_card_number
from .validations import validate_cvv
from .validations import validate_holder


class CreditCard(models.Model):
    """
    Credit Card Model to store data on DB

    """

    # Primary Key Field
    id = models.AutoField(primary_key=True)
    # Expiration Date
    exp_date = CustomDateGeneratedField(max_length=10, validators=[validate_exp_date])
    # Card Holder
    holder = models.CharField(max_length=50, validators=[validate_holder])
    # Card Number
    card_number = CustomEncryptedField(max_length=255, unique=True, validators=[validate_card_number])
    # Verification Code
    cvv = models.IntegerField(blank=True, null=True, validators=[validate_cvv])
    # Card Brand
    brand = models.CharField(max_length=50, blank=True, null=True)

    def save(self, *args, **kwargs):
        cc = CCModule(self.card_number)

        self.brand = cc.get_brand()

        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"CreditCard (id={self.id}, card_number={self.card_number}, holder={self.holder}, exp_date={self.exp_date}, brand={self.brand}, cvv={self.cvv})"
