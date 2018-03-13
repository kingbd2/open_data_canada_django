#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 14:14:07 2018

@author: bking
"""
import re
import requests
import csv
import datetime as dt
import pandas as pd
from bs4 import BeautifulSoup as bs
from time import sleep
from urllib.request import urlopen

### Get all links from the designated URL. ###
def getCSV(url):
    html_page = requests.get(url)
    soup = bs(html_page.text, 'lxml')
    
    for link in soup.findAll('a'):
        current_link = link.get('href')
        if current_link is None:
            continue
        elif current_link.endswith('csv'):
            print('Found CSV: ' + current_link)
            print('Downloading %s' % current_link)
            df = pd.read_csv(current_link, parse_dates=True, encoding='UTF-8')
            
#            sleep(2)
        else: 
            continue
        
    return df



def getXML(url):
    html_page = requests.get(url)
    soup = bs(html_page.text, 'html5lib')
    
    for link in soup.findAll('a', attrs={'href': re.compile("https://")}):
        current_link = link.get('href')
        if current_link.endswith('xml'):
            print('Found xml: ' + current_link)
            print('Downloading %s' % current_link)
            response = urlopen(current_link)
            cr = csv.reader(response)
            sleep(2)
        
    return cr