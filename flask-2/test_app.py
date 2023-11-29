from app import app
from unittest import TestCase
from converter import CurrencyConverter

c = CurrencyConverter()
class ConverterTestCase(TestCase):
    def test_convert_currency(self):
        result = c.convert_curr('USD', 'USD', 1)
        self.assertEqual(result,1)

    def test_generate_symbol(self):
        result = c.generate_symbol("USD")
        self.assertEqual(result,'$')

    # def test_entry_validity(self):
    #     result1 = c.entry_validity('USDd', 'EUW')
    #     self.assertEqual(result1, "Invalid currency code {convert_from} and {convert_to}.")