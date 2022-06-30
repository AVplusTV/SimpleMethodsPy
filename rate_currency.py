
from currency_converter import CurrencyConverter
c = CurrencyConverter()
usd_rate = c.convert(1, 'USD', 'RUB')
euro_rate = c.convert(1, 'EUR', 'RUB')
print(round(usd_rate, 2), round(euro_rate, 2))