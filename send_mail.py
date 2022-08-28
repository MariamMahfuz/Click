import smtplib
from email.message import EmailMessage

import schedule

msg=EmailMessage()
msg['Subject']='Mouse Click Update'
msg['From']='Mariam Binte Mahfuz'
msg['To']='bintemahfuz92@gmail.com'
msg.set_content("My Test")
def mailll():
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login("bintemahfuz92@gmail.com","mbpfftdmdiooufhm")
        smtp.send_message(msg)
        smtp.quit()
        print("Email Sent")

schedule.every(4).seconds.do(mailll())


