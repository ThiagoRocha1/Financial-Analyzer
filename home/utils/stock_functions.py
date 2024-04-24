import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def getStockInfo(stockSymbol: str,interval: str)->dict:
    request_params = {'function':'TIME_SERIES_INTRADAY',
                      'symbol':f'{stockSymbol}',
                      'apikey':'KUKVBJ02YUQK5M0U',
                      'interval':f'{interval}'}
    url = 'https://www.alphavantage.co/query'
    r = requests.get(url, params=request_params)

    # Conferindo se o limite diario da api foi atingido
    if "Information" in r.json() and r.json()["Information"] == "Thank you for using Alpha Vantage! Our standard API rate limit is 25 requests per day. Please subscribe to any of the premium plans at https://www.alphavantage.co/premium/ to instantly remove all daily rate limits.":
        stock_info = {'error':'error'}
        return stock_info
    
    #Se tudo estiver correto
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

def verifyStockInfo(stockSymbol: str)->dict:
    request_params = {'function':'TIME_SERIES_INTRADAY',
                      'symbol':f'{stockSymbol}',
                      'apikey':'KUKVBJ02YUQK5M0U',
                      'interval':'15min'}
    url = 'https://www.alphavantage.co/query'
    r = requests.get(url, params=request_params)

    #Conferindo se é um símbolo válido de ação
    if "Error Message" in r.json():
        stock_info = {'Error Message':'O símbolo da ação não é válido.'}
        return stock_info
    
    #Limite diario da api atingido
    elif "Information" in r.json() and \
        r.json()["Information"] == "Thank you for using Alpha Vantage! Our standard API rate limit is 25 requests per day. Please subscribe to any of the premium plans at https://www.alphavantage.co/premium/ to instantly remove all daily rate limits.":
        stock_info = {'error':'error'}
        return stock_info
    
    else:
        stock_info = {'Success':'É uma ação válida'}
        return stock_info


def sendEmail(bodyMessage: str,arrayOfReceivers: list)-> None:
    try:
        msg = MIMEMultipart()
        msg['Subject'] = "Oportunidade de investimento!"
        msg['From'] = 'mrthiago09@gmail.com'
        receivers = arrayOfReceivers
        password = ''

        body = bodyMessage
        bodyHtml = MIMEText(body, 'html')
        msg.attach(bodyHtml)

        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()
        s.login(msg['From'],password)
        s.sendmail(msg['From'],receivers,msg.as_string().encode('utf-8'))
        print('Email enviado com sucesso!')
    except Exception as e:
        print(f"Erro ao enviar email: {e}")
    finally:
        s.quit()