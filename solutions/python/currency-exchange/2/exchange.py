"""Functions for calculating steps in exchanging currency.

Python numbers documentation: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

Overview of exchanging currency when travelling: https://www.compareremit.com/money-transfer-tips/guide-to-exchanging-currency-for-overseas-travel/
"""



def exchange_money(budget: float, exchange_rate: float) -> float:
    return budget / exchange_rate


def get_change(budget: float, exchanging_value: float) -> float:
    return budget - exchanging_value


def get_value_of_bills(denomination: int, number_of_bills: int) -> float:
    return denomination * number_of_bills


def get_number_of_bills(amount: float, denomination: int) -> float:
    return amount // denomination


def get_leftover_of_bills(amount: float, denomination: int):
    return amount - get_number_of_bills(amount, denomination) * denomination


def exchangeable_value(budget: float, exchange_rate: float, spread: int, denomination: int) -> int:
    spread_val = float(spread) / 100
    actual_rate = exchange_rate + (exchange_rate * spread_val)
    
    in_new_currency = exchange_money(budget, actual_rate)
    leftover = get_leftover_of_bills(in_new_currency, denomination)
    return in_new_currency - leftover
