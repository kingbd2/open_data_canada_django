#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 16:08:03 2018

@author: bking
"""

### Get CSVs and convert to Pandas dataframe

from get_links import getCSV

data_url = "https://open.canada.ca/data/en/dataset/43ea3719-f2ea-4c30-91d2-c8cf9b9b1cef"

data = getCSV(data_url)