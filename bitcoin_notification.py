from requests import Request,Session
import time
#from datetime import datetime
import json
#import pprint

PRICE_LOW_BOUND=30000
BITCOIN_API_URL = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'
WEBHOOKS_URL = 'http://127.0.0.1:5000/webhook'

parameters={
    'slug':'bitcoin',
    'convert':'USD'
}

headers={
    'Accepts':'application/json',
    'X-CMC_PRO_API_KEY':'70c0e50e-f8c5-4324-8463-cacce65052ab'
}

session=Session()
session.headers.update(headers)
#print(123)

def latest_price():
    response=session.get(BITCOIN_API_URL,params=parameters)
    #print(1)
    price=json.loads(response.text)['data']['1']['quote']['USD']['price']
    #pprint.pprint(json.loads(response.text)['data']['1']['quote']['USD']['price'])
    #print(type(response))
    #response_json = response.json()
    #print(response_json)
    #print(price)
    return float(price)

def send_post_to_webhook(value):
    session.post(WEBHOOKS_URL, json=value)

def emergency():
    while True:
        price = latest_price()
        #print(price)
        if price<PRICE_LOW_BOUND:
            send_post_to_webhook(price)

        time.sleep(5 * 60)

if __name__=='__main__':
    emergency()
