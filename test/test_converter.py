from unittest import TestCase

from converter import Currency_Converter

class TestConverter(TestCase):
    """Test the convert and methods"""
    def setUp(self):
        """Test if an instance is created"""
        self.converter = Currency_Converter("USD", "USD", 1000.00)
    
    def test_get_values(self):
        """Test if values are set into correct formar"""
        self.assertEqual(self.converter.get_values(), ("USD", "USD", 1000.00))
     

    def test_get_rate_result(self):
        """Test if the rates values are converted correctly"""
        self.assertEqual(self.converter.get_rate_result("USD", "USD", 1000.00), ("USD", "USD", 1000.00))
   
    def test_get_symbol(self):
        """Test if the correct symbol is retrieved"""
        self.assertEqual(self.converter.get_symbol("USD"),"$")
