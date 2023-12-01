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

class TestApp(TestCase):
    def test_converted(self):
        with app.test_client() as client:
            response = client.post('/converted', data = {'from-curr':'USD', 'to_curr':'EUR', 'amount':'10'})
            html = response.get_data(as_text=True)

            # self.assertIn('<h1>EZ Convert</h1>', html)
            # self.assertEqual(response.status_code, 200)
            # print(response.text)
            