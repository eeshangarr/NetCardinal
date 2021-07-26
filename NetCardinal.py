#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Import DateTime and Speedtest API 

import datetime 
import speedtest

# Loop through Time until Time meets the Given Parameters
while True:
    time = datetime.datetime.now().time()
    if time.hour == 9 and time.minute == 0:
        
# Once Parameters met, use Speedtest API to measure Download Speed, Upload Speed, and Ping 
# Store Download Speed, Upload Speed, and Ping as Variables
        mbps_converter = 1e+6 
    
        d00 = speedtest.Speedtest()
        d1 = d00.download()/mbps_converter
        u1 = d00.upload()/mbps_converter
        p1 = d00.results.ping
    
        print(d1)
        print(u1)
        print(p1)

# Break out of Loop once All of Above is Complete
        break 


# In[ ]:


# Import DateTime and Speedtest API 

import datetime 
import speedtest

# Loop through Time until Time meets the Given Parameters
while True:
    time = datetime.datetime.now().time()
    if time.hour == 10 and time.minute == 0:
        
# Once Parameters met, use Speedtest API to measure Download Speed, Upload Speed, and Ping 
# Store Download Speed, Upload Speed, and Ping as Variables
        mbps_converter = 1e+6
    
        d01 = speedtest.Speedtest()
        d2 = d01.download()/mbps_converter
        u2 = d01.upload()/mbps_converter
        p2 = d01.results.ping
    
        print(d2)
        print(u2)
        print(p2)
 
 # Break out of Loop once All of Above is Complete
        break 


# In[ ]:


# Import DateTime and Speedtest API 

import datetime 
import speedtest

# Loop through Time until Time meets the Given Parameters
while True:
    time = datetime.datetime.now().time()
    if time.hour == 11 and time.minute == 0:
        
# Once Parameters met, use Speedtest API to measure Download Speed, Upload Speed, and Ping 
# Store Download Speed, Upload Speed, and Ping as Variables
        mbps_converter = 1e+6
    
        d02 = speedtest.Speedtest()
        d3 = d02.download()/mbps_converter
        u3 = d02.upload()/mbps_converter
        p3 = d02.results.ping
    
        print(d3)
        print(u3)
        print(p3)
    
# Break out of Loop once All of Above is Complete
        break  


# In[ ]:


# Import DateTime and Speedtest API 

import datetime 
import speedtest

# Loop through Time until Time meets the Given Parameters
while True:
    time = datetime.datetime.now().time()
    if time.hour == 12 and time.minute == 0:
        
# Once Parameters met, use Speedtest API to measure Download Speed, Upload Speed, and Ping 
# Store Download Speed, Upload Speed, and Ping as Variables
        mbps_converter = 1e+6
    
        d03 = speedtest.Speedtest()
        d4 = d03.download()/mbps_converter
        u4 = d03.upload()/mbps_converter
        p4 = d03.results.ping
    
        print(d4)
        print(u4)
        print(p4)

# Break out of Loop once All of Above is Complete
        break 


# In[ ]:


# Import DateTime and Speedtest API 

import datetime 
import speedtest

# Loop through Time until Time meets the Given Parameters
while True:
    time = datetime.datetime.now().time()
    if time.hour == 13 and time.minute == 0:
        
# Once Parameters met, use Speedtest API to measure Download Speed, Upload Speed, and Ping 
# Store Download Speed, Upload Speed, and Ping as Variables
        mbps_converter = 1e+6
    
        d04 = speedtest.Speedtest()
        d5 = d04.download()/mbps_converter
        u5 = d04.upload()/mbps_converter
        p5 = d04.results.ping
    
        print(d5)
        print(u5)
        print(p5)
    
# Break out of Loop once All of Above is Complete
        break        


# In[ ]:


# Import DateTime and Speedtest API 

import datetime 
import speedtest

# Loop through Time until Time meets the Given Parameters
while True:
    time = datetime.datetime.now().time()
    if time.hour == 14 and time.minute == 0:
        
# Once Parameters met, use Speedtest API to measure Download Speed, Upload Speed, and Ping 
# Store Download Speed, Upload Speed, and Ping as Variables
        mbps_converter = 1e+6
    
        d05 = speedtest.Speedtest()
        d6 = d05.download()/mbps_converter
        u6 = d05.upload()/mbps_converter
        p6 = d05.results.ping
    
        print(d6)
        print(u6)
        print(p6)
    
# Break out of Loop once All of Above is Complete
        break 


# In[ ]:


# Import DateTime and Speedtest API 

import datetime 
import speedtest

# Loop through Time until Time meets the Given Parameters
while True:
    time = datetime.datetime.now().time()
    if time.hour == 15 and time.minute == 0:
        
# Once Parameters met, use Speedtest API to measure Download Speed, Upload Speed, and Ping 
# Store Download Speed, Upload Speed, and Ping as Variables
        mbps_converter = 1e+6
    
        d06 = speedtest.Speedtest()
        d7 = d06.download()/mbps_converter
        u7 = d06.upload()/mbps_converter
        p7 = d06.results.ping
    
        print(d7)
        print(u7)
        print(p7)
    
# Break out of Loop once All of Above is Complete
        break 


# In[ ]:


# Import DateTime and Speedtest API 

import datetime 
import speedtest

# Loop through Time until Time meets the Given Parameters
while True:
    time = datetime.datetime.now().time()
    if time.hour == 16 and time.minute == 0:
        
# Once Parameters met, use Speedtest API to measure Download Speed, Upload Speed, and Ping 
# Store Download Speed, Upload Speed, and Ping as Variables
        mbps_converter = 1e+6
    
        d07 = speedtest.Speedtest()
        d8 = d07.download()/mbps_converter
        u8 = d07.upload()/mbps_converter
        p8 = d07.results.ping
    
        print(d8)
        print(u8)
        print(p8)
    
# Break out of Loop once All of Above is Complete
        break  


# In[ ]:


# Import DateTime and Speedtest API 

import datetime 
import speedtest

# Loop through Time until Time meets the Given Parameters
while True:
    time = datetime.datetime.now().time()
    if time.hour == 17 and time.minute == 0:
        
# Once Parameters met, use Speedtest API to measure Download Speed, Upload Speed, and Ping 
# Store Download Speed, Upload Speed, and Ping as Variables
        mbps_converter = 1e+6
    
        d08 = speedtest.Speedtest()
        d9 = d08.download()/mbps_converter
        u9 = d08.upload()/mbps_converter
        p9 = d08.results.ping
    
        print(d9)
        print(u9)
        print(p9)
    
# Break out of Loop once All of Above is Complete
        break  


# In[ ]:


# Graph 1 - Time vs Download Speed

import matplotlib.pyplot as plt # Import MatPlotLib
plt.plot(['09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00'], [d1, d2, d3, d4, d5, d6, d7, d8, d9]) # Define Dataset
plt.ylabel('Download Speed (MBPS)') # Set Y-Axis Label
plt.xlabel('Time (Millitary)') # Set X-Axis Label
plt.title('Time vs Download Speed') # Set Title
plt.savefig('Time vs Download Speed.png') # Save Graph
plt.show() # Show Graph


# In[ ]:


# Graph 2 - Time vs Upload Speed

import matplotlib.pyplot as plt # Import MatPlotLib
plt.plot(['09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00'], [u1, u2, u3, u4, u5, u6, u7, u8, u9]) # Define Dataset
plt.ylabel('Upload Speed (MBPS)') # Set Y-Axis Label
plt.xlabel('Time (Millitary)') # Set X-Axis Label
plt.title('Time vs Upload Speed') # Set Title
plt.savefig('Time vs Upload Speed.png') # Save Graph
plt.show() # Show Graph


# In[ ]:


# Graph 3 - Time vs Ping

import matplotlib.pyplot as plt # Import MatPlotLib
plt.plot(['09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00'], [p1, p2, p3, p4, p5, p6, p7, p8, p9]) # Define Dataset
plt.ylabel('Ping (MS)')# Set Y-Axis Label
plt.xlabel('Time (Millitary)')# Set X-Axis Label
plt.title('Time vs Ping') # Set Title
plt.savefig('Time vs Ping.png') # Save Graph
plt.show() # Show Graph


# In[ ]:


from datetime import date # Import DateTime Library
currentdate = date.today() # Define Today's Date as a Variable
current_date = currentdate.strftime("%m/%d/%y") # Set Today's Date as a New Variable in Month, Day, Year form


# In[ ]:


# Importing Email (smtplib) and Image Attachement Libraries 
import smtplib
import imghdr

#Define Key Email Message Components 
sender = '' # Person Sending Email Message
receiver = '' # Person Receiving Email Message
sender_password = '' # Password of Person Sending Email Message (Required for Mail Server Authentication)
message = 'Network Performance for ' + current_date # Subject of Email with Today's Date

from email.message import EmailMessage # Import Email Message Library
email_message = EmailMessage() #Define the Email Message as a Variable, "email_message"
email_message['Subject'] = message #Define Subject of Email Message
email_message['From'] = sender #Define Email Message Sender
email_message['To'] = receiver #Define Email Message Receiver 

with open('Time vs Download Speed.png', 'rb') as fp: #Open Image File: Time vs Upload Speed.png and Store Under "fp"
    image_file = fp.read() # Define Image File
    email_message.add_attachment(image_file, maintype='image', subtype=imghdr.what(None, image_file)) # Attach Image File and Define Parameters to Send
    
with open('Time vs Upload Speed.png', 'rb') as fp: #Open Image File: Time vs Upload Speed.png and Store Under "fp"
    image_file = fp.read() # Define Image File
    email_message.add_attachment(image_file, maintype='image', subtype=imghdr.what(None, image_file)) # Attach Image File and Define Parameters to Send

with open('Time vs Ping.png', 'rb') as fp: #Open Image File: Time vs Ping.png and Store Under "fp"
    image_file = fp.read() # Define Image File
    email_message.add_attachment(image_file, maintype='image', subtype=imghdr.what(None, image_file)) # Attach Image File and Define Parameters to Send
    
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as sent_email: # Connect to Mail Server 
    sent_email.login(sender,sender_password) # Login to Mail Server (Authentication Requried)
    sent_email.send_message(email_message) # Send Email Message (email_message)

