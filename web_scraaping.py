# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 17:14:10 2019

@author: Muhammed Hassan M
"""

import numpy as np
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup

def getHTMLContent(link):
    html = urlopen(link)
    soup = BeautifulSoup(html, 'html.parser')
    return soup

content = getHTMLContent('https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population')
tables = content.find_all('table')
for table in tables:
    print(table.prettify())
    
# The cell with the country name for each row includes a link to the country webpage on Wikipedia
table = content.find('table', {'class':'wikitable sortable mw-datatable'})
rows = table.find_all('tr')
# List of all links
for row in rows:
    cells = row.find_all('td')
    if len(cells) > 1:
        country_link = cells[1].find('a')
        print(country_link.get('href'))

def getAdditionalDetails(url):
    try:
        country_page = getHTMLContent('https://en.wikipedia.org' + url)
        table = country_page.find('table', {'class': 'infobox geography vcard'})
        additional_details = []
        read_content = False
        for tr in table.find_all('tr'):
            if (tr.get('class') == ['mergedtoprow'] and not read_content):
                link = tr.find('a')
                if (link and (link.get_text().strip() == 'Area' or
                   (link.get_text().strip() == 'GDP' and tr.find('span').get_text().strip() == '(nominal)'))):
                    read_content = True
                if (link and (link.get_text().strip() == 'Population')):
                    read_content = False
            elif ((tr.get('class') == ['mergedrow'] or tr.get('class') == ['mergedbottomrow']) and read_content):
                additional_details.append(tr.find('td').get_text().strip('\n')) 
                if (tr.find('div').get_text().strip() != '•\xa0Total area' and
                   tr.find('div').get_text().strip() != '•\xa0Total'):
                    read_content = False
        return additional_details
    except Exception as error:
        print('Error occured: {}'.format(error))
        return []
data_content = []
for row in rows:
    cells = row.find_all('td')
    if len(cells) > 1:
        print(cells[1].get_text())
        country_link = cells[1].find('a')
        country_info = [cell.text.strip('\n') for cell in cells]
        additional_details = getAdditionalDetails(country_link.get('href'))
        if (len(additional_details) == 4):
            country_info += additional_details
            data_content.append(country_info)

dataset = pd.DataFrame(data_content)