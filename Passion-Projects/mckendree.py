import requests
from bs4 import BeautifulSoup
import pandas as pd

## getting his url 
url = 'https://mckbearcats.com/sports/mens-volleyball/stats/2024'

# if you get 200, it is good
page = requests.get(url)

soup = BeautifulSoup(page.text, features ='html.parser')

table = soup.find('table', class_ = "sidearm-table highlight-column-hover collapse-on-medium accordion")

#< section id="individual-overall-offensive" aria-labelledby="ui-id-9" role="tabpanel" class="ui-tabs-panel ui-corner-bottom ui-widget-content" aria-hidden="false">
count = []
for i in table:
    i.find("col")
    count += i
    print(i)