import re
import requests


def get_stock(symbol):
    try:
        request_fundamentals = requests.get('https://api.robinhood.com/fundamentals/{}/'.format(symbol))
        request_fundamentals.raise_for_status()
        fundamentals = request_fundamentals.json()

        request_quote = requests.get('https://api.robinhood.com/quotes/{}/'.format(symbol))
        request_quote.raise_for_status()
        quote = request_quote.json()
    except requests.exceptions.HTTPError:
        return None

    price = quote.get('last_extended_hours_trade_price') or quote['last_trade_price']

    # Money + Floating Point Arithmetic = BAD.  The only reason we're doing it here?
    # It's fine for display.. Kind of.  Ideally, we'd use a decimal type.

    change = float(price) - float(quote['adjusted_previous_close'])

    # In every case I've found, the company name is In Capitals At
    # The Start Of The Description.
    m = re.match(r'^([A-Z]\S* )*', fundamentals['description'])
    if m:
        name = m.group(0).strip()
    else:
        name = '${}'.format(symbol)

    return {
        'symbol': quote['symbol'],
        'name': name,
        'change': change,
        'percent_change': 100 * change / (float(price) - change),
        'price': float(price),
        'high': float(fundamentals['high']),
        'low': float(fundamentals['low'])
    }
