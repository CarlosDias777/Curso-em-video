from forex_python.converter import CurrencyRates
from forex_python.bitcoin import BtcConverter
c = CurrencyRates()
dolar = c.get_rate('BRL', 'USD')
brl = c.get_rate('USD','BRL')
b = BtcConverter()
btc = b.get_latest_price('BRL')
rs = float(input('Digite o valor em reais:R$ '))
print('O valor de R$ {} convertido para dolar é de USD {:.2f}'.format(rs, dolar*rs))
print('E convertido para BTC é igual a ฿~ {:.8f}'.format(rs/btc))
