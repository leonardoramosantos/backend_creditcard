from cryptography.hazmat.primitives.ciphers import algorithms
from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers import modes
from django.db import models
from django.conf import settings
from binascii import unhexlify

from .functions import get_last_day_of_month_date

class CustomEncryptedField(models.CharField):
    """
    Wrapped field to save cripted data and show decripted data
    Inspiration from: https://cryptography.io/en/latest/hazmat/primitives/symmetric-encryption/

    """
    def from_db_value(self, value, expression, connection):
        """
        Decrypt field value to use on the application.
    
        """

        cipher = Cipher(algorithms.AES(settings.ENCRYPTION_KEY), 
                                       modes.CBC(settings.ENCRYPTION_INIT_VECTOR))
        decryptor = cipher.decryptor()
        result = decryptor.update(bytes.fromhex(value)) + decryptor.finalize()

        return result.decode("utf-8")

    def get_prep_value(self, value):
        """
        Encrypt value to save on the database.
        Saves in hexadecimal to make easy the convertion proccess

        """

        value = str(value).replace(" ", "")

        cipher = Cipher(algorithms.AES(settings.ENCRYPTION_KEY), 
                                       modes.CBC(settings.ENCRYPTION_INIT_VECTOR))
        encryptor = cipher.encryptor()
        value = encryptor.update(bytes(value, "utf-8")) + encryptor.finalize()

        return super().get_prep_value(value.hex())


class CustomDateGeneratedField(models.CharField):
    """
    Field to process string input and find the last day of month to save on DB

    """

    def get_prep_value(self, value):
        
        if isinstance(value, str):
            [month, year] = value.split("/")

            value = get_last_day_of_month_date(int(year), int(month))

        return super().get_prep_value(value)