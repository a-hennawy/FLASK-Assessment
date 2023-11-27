from forex_python.converter import CurrencyRates

c = CurrencyRates()

class CurrencyConverter:

    def __init__(self):
        self.curr_list = []
        curr_dict = c.get_rates('USD')
        curr_dict['USD'] = 0
        for curr in curr_dict.keys():
            self.curr_list.append(curr)

    def convert_curr(self,con_from, con_to,amount):
        self.con_from = con_from
        self.con_to = con_to
        self.amount = amount
        rate = c.convert(self.con_from, self.con_to, self.amount)
        return round(rate,2)
    
