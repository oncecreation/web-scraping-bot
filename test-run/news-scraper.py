#%%
# import libraries
import requests
from bs4 import BeautifulSoup

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
all_items = []
for item in content:
    all_items.append(item.text)

print("Total items extracted, including headlines : \n", len(all_items))
# %%
# Parse 'Most Read' news items into CSV 