# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 11:54:26 2019

@author: Asus
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 03:09:10 2019

@author: Asus
"""
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
import pandas as pd
#df = pd.read_excel('algorythm.xlsx', sheetname='2ND ROUND RSVP')


#for i in range(len(df)):
def mailintruder():
#    print(photo)
#    cv2.imwrite(filename, frame)
#    print("hello")
    fromaddr = "iosdmait@gmail.com"
    toaddr = "singhaldeepali96@gmail.com"
    msg = MIMEMultipart() 
    msg['From'] = fromaddr 
    msg['To'] = toaddr 
    msg['Subject'] = "Intruder Alert"    
    body = "Hey ,\n We detected a intruder at your home. Please look into the matter. Photograph is attached"
    
    # attach the body with the msg instance 
    msg.attach(MIMEText(body, 'plain')) 
    
    # open the file to be sent 
    filename = "intruder.png"
    attachment = open("intruder.png", "rb") 
    # instance of MIMEBase and named as p 
    p = MIMEBase('application', 'octet-stream') 
    # To change the payload into encoded form 
    p.set_payload((attachment).read()) 
    # encode into base64 
    encoders.encode_base64(p) 
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
    msg.attach(p) 

    
    # creates SMTP session 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    # start TLS for security 
    s.starttls() 
    s.login(fromaddr, "mohitbhadwa") 
    text = msg.as_string() 
    # sending the mail 
    s.sendmail(fromaddr, toaddr, text) 
    print("success")
    s.quit() 
