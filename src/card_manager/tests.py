from datetime import date

from django.test import TestCase

from .exceptions import HolderSizeException
from .exceptions import InvalidCardNumberException
from .exceptions import InvalidCVVException
from .exceptions import InvalidDateException
from .exceptions import InvalidMonthException
from .exceptions import InvalidYearException
from .functions import get_last_day_of_month_date
from .validations import validate_card_number
from .validations import validate_cvv
from .validations import validate_exp_date
from .validations import validate_holder

class ExpDateValidationsTestCase(TestCase):
    def test_happy_path(self):
        self.assertTrue(validate_exp_date("01/3000"), "Date should be valid")

    def test_invalid_date_exception(self):
        try:
            validate_exp_date("aaaa")
            self.fail("No exception thrown")
        except InvalidDateException:
            pass
        except Exception:
            self.fail("Exception should be InvalidDateException")

        try:
            validate_exp_date("02/-001")
            self.fail("No exception thrown")
        except InvalidDateException:
            pass
        except Exception:
            self.fail("Exception should be InvalidDateException")

    def test_invalid_year(self):
        try:
            validate_exp_date("02/2022")
            self.fail("No exception thrown")
        except InvalidYearException:
            pass
        except Exception:
            self.fail("Exception should be InvalidYearException")

        try:
            validate_exp_date("02/0014")
            self.fail("No exception thrown")
        except InvalidYearException:
            pass
        except Exception:
            self.fail("Exception should be InvalidYearException")
    
    def test_invalid_month(self):
        try:
            validate_exp_date("01/2023")
            self.fail("No exception thrown")
        except InvalidMonthException:
            pass
        except Exception:
            self.fail("Exception should be InvalidMonthException")

        try:
            validate_exp_date("02/2023")
            self.fail("No exception thrown")
        except InvalidMonthException:
            pass
        except Exception:
            self.fail("Exception should be InvalidMonthException")

        try:
            validate_exp_date("15/2023")
            self.fail("No exception thrown")
        except InvalidMonthException:
            pass
        except Exception:
            self.fail("Exception should be InvalidMonthException")


class HolderValidationsTestCase(TestCase):
    def test_happy_path(self):
        self.assertTrue(validate_holder("Leonardo Ramos dos Santos"))

    def test_holder_exception(self):
        try:
            validate_holder("")
            self.fail("No exception thrown")
        except HolderSizeException:
            pass
        except Exception:
            self.fail("Exception should be HolderSizeException")
        
        #                    0         1         2         3         4         0
        try:
            validate_holder("012345678901234567890123456789012345679801234567890")
            self.fail("No exception thrown")
        except HolderSizeException:
            pass
        except Exception:
            self.fail("Exception should be HolderSizeException")


class CardNumberValidationsTestCase(TestCase):
    def test_happy_path(self):
        self.assertTrue(validate_card_number("5575132050201776"))

    def test_card_number_exception(self):
        try:
            validate_card_number("")
            self.fail("No exception thrown")
        except InvalidCardNumberException:
            pass
        except Exception:
            self.fail("Exception should be InvalidCardNumberException")


class CVVValidationsTestCase(TestCase):
    def test_happy_path(self):
        self.assertTrue(validate_cvv(123))

    def test_cvv_exception(self):
        try:
            validate_cvv("")
            self.fail("No exception thrown")
        except InvalidCVVException:
            pass
        except Exception:
            self.fail("Exception should be InvalidCVVException")

    def test_cvv_length_exception(self):
        try:
            validate_cvv(1)
            self.fail("No exception thrown")
        except InvalidCVVException:
            pass
        except Exception:
            self.fail("Exception should be InvalidCVVException")
        
        try:
            validate_cvv(12345)
            self.fail("No exception thrown")
        except InvalidCVVException:
            pass
        except Exception:
            self.fail("Exception should be InvalidCVVException")


class LastDayOfMontTestCase(TestCase):
    def test_last_day_of_month(self):
        self.assertEquals(date(2023, 1, 31), get_last_day_of_month_date(2023, 1))
        self.assertEquals(date(2023, 2, 28), get_last_day_of_month_date(2023, 2))
        self.assertEquals(date(2020, 2, 29), get_last_day_of_month_date(2020, 2))