# set up converter that will three inputs 
# import forex and and methods needed
from forex_python.converter import CurrencyRates, CurrencyCodes

from forex import c_rates, c_symbol

c_rates = CurrencyRates(force_decimal=True)
# Decimal() Do not want ints passed in as strings

c_symbol = CurrencyCodes()

class Currency_Converter:
    """Converts a currency from one value to another and gives the result
    """
    def __init__(self, from_curr, to_curr, amount):
        """Passing in the values to be converted"""
        self.from_curr = from_curr
        self.to_curr = to_curr
        self.amount = amount
        
         
    
    def __repr__(self):
        """A representation of the Current Converter"""
        cls = self.__class__.__name__
        return f"""{cls}(from_curr={self.from_curr}), (to_curr={self.to_curr}),
        (amount={self.amount})"""
    
    def get_values(self):
        """Shows the values from handling in other methods"""
        values = self.from_curr.upper(), self.to_curr.upper(), self.amount
        return values

    def get_rate_result(self, from_curr, to_curr, amount):
        """Substitues the key/value pair in to a string to be converted by forex"""
        result = c_rates.convert(from_curr, to_curr, amount)
        
        return result
    

    def check_is_valid(self, from_curr, to_curr, amount):
        """Checks if values are valid, if not displays error message"""
        rates = c_rates.get_rates("USD")

        if not from_curr in rates:
            msg = f"Not a valid code:{from_curr}"
            return msg
        if not to_curr in rates:
            msg = f"Not a valid code:{to_curr}"
            return msg

        if not isinstance(amount, int):
            msg = f"{amount} is not a valid amount"
            return msg

          
    def get_symbol(self, to_curr):
        """Gets the currency symbol from the datebase"""
        symbol = c_symbol.get_symbol(to_curr)
        return symbol
        




