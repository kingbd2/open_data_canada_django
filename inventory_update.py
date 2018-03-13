#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 14:54:56 2018

@author: bking
"""
from urllib.request import urlopen
import get_links
import pandas as pd

###Load latest version of Open Data Canada inventory###
#load_inventory.py

#Load inventory from CSV from Open Data Canada

inventory_url = "https://open.canada.ca/data/en/dataset/4ed351cf-95d8-4c10-97ac-6b3511f359b7"

df = getCSV(inventory_url)

def clean_inventory(df):

    #Remove French columns that contain "fr" from data
    df_names = list(df)
    for names in df_names:
        if "fr" in str(names):
            del df[names]
        
    #Remove rows that represent datasets that cannot be downloaded
    mask = df['portal_url_en'].isnull() 
    data_dl = df[-mask]    
    #Remove all error nulls ie. "N /A" instead of null
    data_dl = data_dl[data_dl.portal_url_en != "N/ A"]

    #Removing data sets based on criteria:
    # - Canada-wide (not province-specific)
    # - No date_published
    data_dl = data_dl[data_dl.date_published != "quarterly trimestrielle"]
    data_dl = data_dl.drop(['date_released'], axis=1)
    return data_dl
    


data_dl['datetime'] = pd.to_datetime(df['date_published'], format="%m/%d/%Y")
    
data_link = input("Copy the data you want to work with as a csv file link here.") 
data_test = pd.read_csv(data_link)
