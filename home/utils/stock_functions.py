import requests

def getStockInfo(stockSymbol,interval):
    stock_info = {'error':'Limite do uso da api diário atingido, as informações não serão processadas.'}

    request_params = {'function':'TIME_SERIES_INTRADAY',
                      'symbol':f'{stockSymbol}',
                      'apikey':'KUKVBJ02YUQK5M0U',
                      'interval':f'{interval}'}
    url = 'https://www.alphavantage.co/query'
    r = requests.get(url, params=request_params)
    # Conferindo se o limite diario da api foi atingido
    if "Information" in r.json() and r.json()["Information"] == "Thank you for using Alpha Vantage! Our standard API rate limit is 25 requests per day. Please subscribe to any of the premium plans at https://www.alphavantage.co/premium/ to instantly remove all daily rate limits.":
        return stock_info
    
    if r.status_code == 200:
        data = r.json()

        meta_data = data["Meta Data"]
        symbol = meta_data["2. Symbol"]
        last_refreshed= meta_data["3. Last Refreshed"]
        interval_analysis = meta_data["4. Interval"]

        times_series = data[f'Time Series ({interval_analysis})']
        day = times_series[f'{last_refreshed}']
        open_price = day["1. open"]
        close_price = day["4. close"]
        highest_price = day["2. high"]
        lowest_price = day["3. low"]
        volume = day["5. volume"]

        stock_info = {
            'symbol':symbol,
            'interval':interval_analysis,
            'open_price':open_price,
            'close_price':close_price,
            'highest_price':highest_price,
            'lowest_price':lowest_price,
            'volume':volume
        }

    return stock_info