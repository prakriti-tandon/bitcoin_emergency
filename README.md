# bitcoin_emergency
This project sends me an emergency email alert whenever bitcoin price falls below a threshold value. 

server.py - running this file creates a webhook. Trigger for webhook: a POST request. Action caused by trigger: sends an emergency email

bitcoin_notification.py - running this file requests a quote from Coin Market API, and sends a POST request to webhook if bitcoin price is below a threshold 
value (here, 30000 USD)

bitcoin_email.py - (not to be run) imported by server.py and used to send an email as an emergency alert 
