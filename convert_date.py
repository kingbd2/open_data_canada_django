#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 21:39:23 2018

@author: bking
"""

import datetime as dt
import pandas as pd
import re
import numpy as np


def convert_date(df):
    
    print(list(df))
    date_col = input("Indicate name of date column:") 
    #date_parse = input("What format do you want the date to be in?") 
    
    df[date_col] = df[date_col].astype(str).apply(lambda x: x.replace('/','-').strip())
    df[date_col] = df[date_col].apply(lambda x: str(x) + "-01-01" if len(str(x))==4 else x)
    df[date_col] = df[date_col].apply(lambda x: np.nan if 'n' in str(x) else x)  
    
    df[date_col] = pd.to_datetime(df[date_col])
    
    return df



 ### Extras ###   
#re.sub("[^0-9]", "", "sdkjh987978asd098as0980a98sd"





#'%Y-%m-%d'