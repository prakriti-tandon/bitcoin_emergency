#webhook receiver
from flask import Flask, request, abort
import bitcoin_email
import bitcoin_notification

app=Flask(__name__)

@app.route('/webhook',methods=['POST'])


#def sendpost():
    #price = bitcoin.get_latest_bitcoin_price()
    #bitcoin.post_ifttt_webhook(price)

def webhook():
    #print(12345)
    if request.method=='POST':
        print(request.json)
        bitcoin_email.send(request.json,bitcoin_notification.PRICE_LOW_BOUND)
        return 'success',200

    else:
        abort(400)

if __name__=='__main__':
    app.run()
