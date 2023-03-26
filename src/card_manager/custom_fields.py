from cryptography.fernet import Fernet
from django.db import models
from django.conf import settings

from .functions import get_last_day_of_month_date

class CustomEncryptedField(models.CharField):
    """
    Wrapped field to save cripted data and show decripted data
    Inspiration from: https://www.geeksforgeeks.org/how-to-encrypt-and-decrypt-strings-in-python/

    """
    def from_db_value(self, value, expression, connection):

        fernet = Fernet(settings.ENCRYPTION_KEY)
        result = fernet.decrypt(value.encode()).decode("utf-8")

        return result

    def get_prep_value(self, value):

        value = str(value).replace(" ", "")

        fernet = Fernet(settings.ENCRYPTION_KEY)
        value = fernet.encrypt(value.encode()).decode()

        return super().get_prep_value(value)


class CustomDateGeneratedField(models.CharField):
    """
    Field to process string input and find the last day of month to save on DB

    """

    def get_prep_value(self, value):
        
        if isinstance(value, str):
            [month, year] = value.split("/")

            value = get_last_day_of_month_date(int(year), int(month))

        return super().get_prep_value(value)