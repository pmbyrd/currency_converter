# set up converter that will three inputs 
# import forex and and methods needed
from forex_python.converter import CurrencyRates, CurrencyCodes, Decimal

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
    
    def get_value_to_convert(self):
        """Substitues the key/value pair in to a string to be converted by forex"""
        return self.from_curr, self.to_curr, Decimal(self.amount)

    # def check_is_valid(self):
    #     """Checks if values are correct, if not displays error message"""

    #     if self.from_curr.upper(): 
        
        

# values = Currency_Converter("USD", "INR", 100)
# get_rates = Currency_Converter.get_value_to_convert(values)
# print(values, get_rates)
