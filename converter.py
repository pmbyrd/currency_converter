# set up converter that will three inputs 
# import forex and and methods needed
from forex_python.converter import CurrencyRates, CurrencyCodes, Decimal

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
        values = self.from_curr.upper(), self.to_curr.upper(), Decimal(self.amount)
        return values

    def get_rate_result(self, from_curr, to_curr, amount):
        """Subs the key/value pair in to a string to be converted by forex"""
        converter_amount = c_rates.convert(from_curr, to_curr, amount)
        result = round(converter_amount, 2)

        return result
    
    def check_is_valid_from(self, from_curr):
        """Checks if the from currency is valid"""
        rates_dict = c_rates.get_rates("USD")
        from_curr = from_curr.upper()
        rates = rates_dict.keys()
        msg = None 

        if from_curr not in rates:
            msg = f"Invalid currency {from_curr}. Please try again."
            return msg
        else:
            return msg
        
    def check_is_valid_to(self, to_curr):
        """Checks if the to currency is valid"""
        rates_dict = c_rates.get_rates("USD")
        to_curr = to_curr.upper()
        rates = rates_dict.keys()
        msg = None 

        if to_curr not in rates:
            msg = f"Invalid currency {to_curr}. Please try again."
            return msg
        else:
            return msg
        
    def check_is_valid_amount(self, amount):
        """Checks if the amount is valid"""
        msg = None
        if not isinstance(amount, int or float or Decimal):
            msg = "Please enter a valid amount"
            return msg
        else:
            amount = Decimal(amount)
            return msg
        
        

    # def check_is_valid(self, from_curr, to_curr, amount):
    #     """Checks if values are valid, if not displays error message"""
    #     rates_dict = c_rates.get_rates("USD")
    #     rates = rates_dict.keys()
    #     msg = None 

    #     if from_curr not in rates:
    #         msg = f"Invalid currency {from_curr}. Please try again."
    #         # return msg
     
    #     if to_curr not in rates:
    #         msg = f"Invalid currency {to_curr}. Please try again."
    #         # return msg
        
    #     if not isinstance(amount, Decimal):
    #         msg = "Please enter a valid amount"
    #         # return msg
          
    def get_symbol(self, to_curr):
        """Gets the currency symbol from the database"""
        symbol = c_symbol.get_symbol(to_curr)
        return symbol

# converter = Currency_Converter("USD", "EUR", 100).check_is_valid()
# values = converter.get_values()
# print(values)

# converter.check_is_valid()



