import  requests
import  json
from config import keys
class ConvertionException(Exception):
    pass
class CurrentConverter:

    @staticmethod
    def get_price(quote: str, base: str, amount: str):

        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}.')
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'{quote} - такой валюты к конвертации нет в боте ')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'{base} - такой валюты к конвертации нет в боте ')

        try:
            amount = int(amount)
        except ValueError:
            raise ConvertionException(f'Некорректный формат ввода суммы для конвертации {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = float(json.loads(r.content)[keys[base]])
        return total_base*amount
#