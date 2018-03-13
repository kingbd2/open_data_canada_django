#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 02:00:45 2018

@author: bking
"""
def export_csv(df):
    file_name = input("Name your updated CSV file:") 
    df.to_csv(file_name, sep=',', index=False, encoding='utf-8')
