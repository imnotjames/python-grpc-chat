from chat.stock import get_stock
import pytest


def test_url(requests_mock):
    fundamentals_json_fixture = '''
        {
            "open": "110.430000",
            "high": "114.810000",
            "low": "109.780000",
            "volume": "454909.000000",
            "average_volume_2_weeks": "2126185.500000",
            "average_volume": "1821075.135500",
            "high_52_weeks": "128.440000",
            "dividend_yield": "0.000000",
            "low_52_weeks": "55.330000",
            "market_cap": "9989197800.000000",
            "pe_ratio": null,
            "shares_outstanding": "89476870.000000",
            "description": "Wayfair, Inc. engages in an online home furnishing store. It offers a selection of home furnishings and decor across all styles and price points. It operates through the U.S. and International segments. The U.S. segment consists of amounts earned through product sales through the Company's five distinct sites in the U.S. and through websites operated by third parties in the U.S. The International segment is composed of earnings through products sales in international sites. The company was founded by Steven K. Conine and Niraj S. Shah in May 2002 and is headquartered in Boston, MA.",
            "instrument": "https://api.robinhood.com/instruments/6390d8af-27a8-4768-b483-c4f7abd1f602/",
            "ceo": "Niraj S. Shah",
            "headquarters_city": "Boston",
            "headquarters_state": "Massachusetts",
            "sector": "Retail Trade",
            "num_employees": 7751,
            "year_founded": 2002
        }
    '''

    quotes_json_fixture = '''
        {
            "ask_price": "114.350000",
            "ask_size": 20400,
            "bid_price": "114.340000",
            "bid_size": 1200,
            "last_trade_price": "114.500000",
            "last_extended_hours_trade_price": "114.500000",
            "previous_close": "111.640000",
            "adjusted_previous_close": "111.640000",
            "previous_close_date": "2018-08-03",
            "symbol": "W",
            "trading_halted": false,
            "has_traded": true,
            "last_trade_price_source": "consolidated",
            "updated_at": "2018-08-06T20:39:37Z",
            "instrument": "https://api.robinhood.com/instruments/6390d8af-27a8-4768-b483-c4f7abd1f602/"
        }
    '''

    requests_mock.get('https://api.robinhood.com/fundamentals/W/', text=fundamentals_json_fixture)
    requests_mock.get('https://api.robinhood.com/quotes/W/', text=quotes_json_fixture)

    stock = get_stock('W')

    assert stock['symbol'] == 'W'
    assert stock['name'] == 'Wayfair, Inc.'
    assert stock['change'] == pytest.approx(2.85, 0.1)
    assert stock['percent_change'] == pytest.approx(2.56, 0.1)
    assert stock['price'] == pytest.approx(114.5, 0.1)
    assert stock['high'] == pytest.approx(114.5, 0.1)
    assert stock['low'] == pytest.approx(114.81, 0.1)
    assert stock['price'] == pytest.approx(109.78, 0.1)

