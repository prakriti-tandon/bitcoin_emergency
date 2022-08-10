import smtplib
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS=''#insert your email id here - not disclosed mine for privacy
EMAIL_PASSWORD=''#insert authorisation key for your email id


def send(value,low_bound):

    msg=EmailMessage()
    msg['Subject']='BITCOIN PRICE HAS FALLEN!'
    msg['From']=EMAIL_ADDRESS
    msg['To']='testprogram130@gmail.com'
    msg.set_content('Bitcoin price has fallen below '+str(low_bound)+'!'+'The current price is '+str(value)+'!')

    #with open('dog.jpg','rb') as f:
        #file_data=f.read()
        #file_type=imghdr.what(f.name)
        #file_name=f.name

    #msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
        smtp.send_message(msg)
