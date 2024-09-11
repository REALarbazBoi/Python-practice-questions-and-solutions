class CurrencyConverter:

    def __init__(self, currency, rate):
        self.currency = currency
        self.rate = rate

    def set_currency(self,curr):
        self.currency = curr

    def get_currency(self):
        return self.currency

    def set_rate(self,r):
        self.rate = r

    def get_rate(self):
        return self.rate

    def convert(self, amount):
        return self.rate * amount


c = CurrencyConverter("USD",70)
c.set_currency("AUD")
c.set_rate(60)
print(c.convert(1000))