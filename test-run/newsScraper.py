#%%
# import libraries
import requests
from bs4 import BeautifulSoup
import csv

print("All libraries imported successfully.")


# %%
# webpage url
url = "https://yle.fi/news"

# get html content
r =  requests.get(url)
text = r.text

# make soup and filter list items  
soup = BeautifulSoup(text, features='lxml')

# filter soup by class for 'Most Read' news items
s = soup.find('div', class_= 'MinimalHeadlines__Container-sc-zhu28g-0 kLTbWH')
content = s.find_all('a')

# iterate list and collect items in list
allItems = []
for item in content:
    allItems.append(item.text)
print('Total items extracted, including headlines : ', len(allItems),'\n')

# Parse 'Most Read' news items into CSV using built-in 'csv'
myFile =  open('newsToday.csv', 'w')
writer = csv.writer(myFile, delimiter='\n')
writer.writerow(allItems)
myFile.close()

# read csv content
myCsv = open('newsToday.csv','r')
print("Today's NEWS :")
print(myCsv.read())

# %%
# Send csv file to email using built-in 'smtplib' & 'email'
import smtplib
from email.message import EmailMessage
import datetime

# read content from CSV to email content
with open('newsToday.csv') as news:
    msg = EmailMessage()
    msg.set_content(news.read())
print('Content written to email\n')

# intialize essential email information
today = datetime.datetime.now().strftime('%c')
msg['Subject'] = f"Headlines for {today}"
msg['From'] = 'pokiphd@gmail.com'
msg['To'] = 'prakirthgovardhanam@yahoo.com'
print('Updated essential information\n')

# send email via SMTP server
server = smtplib.SMTP('')

# identify and secure server
server.ehlo()
server.starttls()
server.ehlo()

# import login details
import os
from dotenv import load_dotenv
load_dotenv('.env')

userName = os.getenv('yahooId')
password = os.getenv('yahooPwd')

# send email
server.login(userName, password)
server.send_message(msg)
server.quit()
print('Sent email!\n')
# %%
