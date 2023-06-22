# import forex and and methods needed
from forex_python.converter import CurrencyRates, CurrencyCodes

c_rates = CurrencyRates(force_decimal=True)
# Decimal() Do not want ints passed in as strings

c_symbol = CurrencyCodes()

rates = c_rates.get_rates("USD")

rates_lst = rates.keys()
