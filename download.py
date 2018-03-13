#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 14:14:07 2018

@author: bking
"""
import re
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import urllib.request, json 


### Set URL ####
url = "https://open.canada.ca/data/en/dataset/aa45f4f3-cbf9-4f28-b108-abf656776e25"

### Get all links from the designated URL. ###

def getLinks(url):
    html_page = requests.get(url)
    soup = bs(html_page.text, 'html5lib')
    links = []
 
    for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
        links.append(link.get('href'))
 
    return links
    
links = getLinks(url)
