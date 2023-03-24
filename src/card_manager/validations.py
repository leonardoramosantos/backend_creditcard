import re

from datetime import datetime
from creditcard import CreditCard

from .exceptions import HolderSizeException
from .exceptions import InvalidCardNumberException
from .exceptions import InvalidDateException
from .exceptions import InvalidMonthException
from .exceptions import InvalidYearException

def validate_exp_date(exp_date):
    """
    Validations for the field exp_date

    """

    date_pattern = re.compile(r"[0-9]{2,}/[0-9]{4,}")

    if not re.fullmatch(date_pattern, exp_date):
        raise InvalidDateException("Date format not suported. Only accepts MM/YYYY")

    [month, year] = exp_date.split("/")
    if int(year) < datetime.now().year:
        raise InvalidYearException("Year is lower than current year")

    if int(month) < datetime.now().month and \
            int(year) <= datetime.now().year:
        raise InvalidMonthException("Month is lower than current month")

    if int(month) > 12 or int(month) <= 0:
        raise InvalidMonthException("Month must be a number between 1 and 12")
    

    return True

def validate_holder(holder):
    """
    Field Holder validations

    """

    if len(holder) < 2 or len(holder) > 50:
        raise HolderSizeException("Holder must have from 2 to 50 characters")

    return True

def validate_card_number(card_number):
    """
    Validations for Card Number field

    """

    cc = CreditCard(card_number)
    if not cc.is_valid():
        raise InvalidCardNumberException("Invalid Card Number")

    return True