#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""load character data from my web source or local and provide into a file"""
import urllib.request, pprint
_published_csv = r'https://docs.google.com/spreadsheets/d/e/2PACX-1vS7VtGA2e06j226OnbwcMXzk2z1KyUqfarZLpHaSLJVUCwplbaVrQvKxbrEEEYnJWKeHcAGyoAVqKgW/pub?gid=1914483541&single=true&output=csv'

def get_web_csv(link = _published_csv):
    """load a csv file from the web like a published google sheet"""
    with open('local_data.csv', 'wb') as csv:
        source = urllib.request.urlopen(link)
        csv.write(source.read())    #_pp.pprint(csv_file)

if __name__=="__main__":
    get_web_csv(_published_csv)