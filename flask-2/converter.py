from forex_python.converter import CurrencyRates, Decimal, CurrencyCodes, RatesNotAvailableError

currency = CurrencyRates()
symbol = CurrencyCodes() 


class CurrencyConverter:

    def __init__(self):
        self.curr_list = []
        curr_dict = currency.get_rates('USD')
        curr_dict['USD'] = 0
        for curr in curr_dict.keys():
            self.curr_list.append(curr)

    def convert_curr(self,convert_from, convert_to,amount):
        self.convert_from = convert_from
        self.convert_to = convert_to
        self.amount = amount

        conversion = currency.convert(self.convert_from, self.convert_to,
                                Decimal(self.amount))
        return round(conversion,2)
    
    def generate_symbol(self, currency_code):
        curr_symbol = symbol.get_symbol(currency_code)
        return curr_symbol
    
    # def entry_validity(self,convert_from, convert_to):

    #     if convert_from not in self.curr_list:
    #         if convert_to not in self.curr_list:
    #             return (f"Invalid currency code {convert_from} and {convert_to}.")
                           
    #     elif convert_to not in self.curr_list:
    #             return (f"Invalid currency code {convert_to}.")
        # elif not isinstance(amount, int):
        #     return (f"invalid amount of {amount}")
        

        # if convert_to not in self.curr_list:
        #     return (f"Invalid currency code {convert_to}")
        # if amount == False:
        #     return (f"Invalid amount {amount}")
            

         
