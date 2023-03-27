import calendar
from datetime import date

def get_last_day_of_month_date(year, month):
    """
    Function to return the last day of a given month
    Inspiration came from: https://pynative.com/python-get-last-day-of-month/

    """

    last_day = calendar.monthrange(year, month)[1]

    return date(year, month, last_day).strftime("%Y-%m-%d")
