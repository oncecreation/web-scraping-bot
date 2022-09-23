#%%
# import libraries
import selenium
from selenium import webdriver
import requests
from bs4 import BeautifulSoup

print("All libraries imported successfully.")

# %%
# USING SELENIUM
# set selenium webdriver PATH - https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/
# using Driver Management Software
# selenium version 4+

import selenium
import webdriver_manager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# initialise --- webdriver not detected--error
driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

# run driver for url
url = "https://yle.fi/news"
driver.get(url)

# provide full XPath of top article
news_path = "/html/body/div[1]/div[2]/div/div[1]/div[1]/a"
link = driver.find_element(news_path)

# get headline --time out error
print(link.text)

# %%
# USING REQUESTS
# use requests for YLE
import requests
from bs4 import BeautifulSoup

url = "https://yle.fi/news"

# get html content
r =  requests.get(url)
text = r.text

# make soup and filter list items
soup = BeautifulSoup(text, features='lxml')
items = soup.find_all('li')

# iterate list and collect items in list
all_items = []
for item in items:
    all_items.append(item.text)

print("Total items extracted, including headlines : \n", len(all_items))
# %%
