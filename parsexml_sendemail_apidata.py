
"""
	The script reads api, email id from given xml file. it takes longitude & latitude from user. sends city, count name info. on emailid.
	requiremnts- python 3
	note- please provide your email id password at below metioned section.
	athor-chetan pawar
"""

import requests
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import xml.etree.ElementTree as ET

password = #password

tree = ET.parse("config.xml")
root = tree.getroot()

api = ""
email = ""

for desc in root.iter("API_URL"):
    api = desc.text
for desc in root.iter("EMAIL_ID"):
    email = desc.text


lat = input("Enter latitude:")
lon = input("Enter longitude:")

url = api+"&format=json"
url = url.replace("LATITUDE",str(lat))
url = url.replace("LONGITUDE",str(lon))

res = requests.get(url)
json_data = res.json()
city=((json_data[0]['display_name']).split(","))[1]
state=((json_data[0]['display_name']).split(","))[3]
country=((json_data[0]['display_name']).split(","))[5]

message = MIMEMultipart()
message["From"] = email
message["To"] = email
message["Subject"] = "Message from python script"
body =str( " city=" + city + "| state=" + state + "| country=" + country)
message.attach(MIMEText(body, "plain"))

s = smtplib.SMTP('smtp.gmail.com', 587) 
s.starttls() 
s.login(email, password)         #put your email id and password here
message = message.as_string()
s.sendmail(email,email,message)
s.quit() 

print("Email sent successfully!")
