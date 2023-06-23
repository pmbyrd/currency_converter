# set up converter that will three inputs 
# import forex and and methods needed
from forex_python.converter import CurrencyRates, CurrencyCodes, Decimal

from forex import c_rates, c_symbol

c_rates = CurrencyRates(force_decimal=True)
# Decimal() Do not want ints passed in as strings

c_symbol = CurrencyCodes()

class Currency_Converter:
    """Converts a currency from one value to another and gives the result"""

    def __init__(self, from_curr, to_curr, amount):
        """Passing in the values to be converted"""
        self.from_curr = from_curr
        self.to_curr = to_curr
        self.amount = Decimal(str(amount))
        self.validate_inputs()

    def __repr__(self):
        """A representation of the Currency Converter"""
        cls = self.__class__.__name__
        return f"{cls}(from_curr={self.from_curr}), (to_curr={self.to_curr}), (amount={self.amount})"

    def validate_inputs(self):
        """Validates the input values"""
        if self.check_is_valid_from(self.from_curr):
            raise ValueError(f"Invalid currency {self.from_curr}. Please try again.")

        if self.check_is_valid_to(self.to_curr):
            raise ValueError(f"Invalid currency {self.to_curr}. Please try again.")

        if self.check_is_valid_amount(self.amount):
            raise ValueError("Please enter a valid amount.")


    def get_rate_result(self, from_curr, to_curr, amount):
        """Substitutes the key/value pair to a string to be converted by forex"""
        converter_amount = c_rates.convert(from_curr, to_curr, amount)
        result = round(converter_amount, 2)
        return result

    def check_is_valid_from(self, from_curr):
        """Checks if the from currency is valid"""
        rates_dict = c_rates.get_rates(base_cur="USD")
        from_curr = from_curr.upper()
        rates = rates_dict.keys()
        return from_curr != "USD" and from_curr not in rates

    def check_is_valid_to(self, to_curr):
        """Checks if the to currency is valid"""
        rates_dict = c_rates.get_rates(base_cur="USD")
        to_curr = to_curr.upper()
        rates = rates_dict.keys()
        return to_curr != "USD" and to_curr not in rates

    def check_is_valid_amount(self, amount):
        """Checks if the amount is valid"""
        return not isinstance(amount, Decimal) or amount <= Decimal(0)


          
    def get_symbol(self, to_curr):
        """Gets the currency symbol from the database"""
        symbol = c_symbol.get_symbol(to_curr)
        return symbol





