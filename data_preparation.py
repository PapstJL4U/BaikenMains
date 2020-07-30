#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""load character data from my web source or local and provide into a file"""
import urllib.request, translation
import pandas as pd
import googlesheet
from datetime import date
from bs4 import BeautifulSoup as BS

_published_csv = r'https://docs.google.com/spreadsheets/d/e/2PACX-1vS7VtGA2e06j226OnbwcMXzk2z1KyUqfarZLpHaSLJVUCwplbaVrQvKxbrEEEYnJWKeHcAGyoAVqKgW/pub?gid=1914483541&single=true&output=csv'
_ggxrdcom_csv = r'https://docs.google.com/spreadsheets/d/e/2PACX-1vS7VtGA2e06j226OnbwcMXzk2z1KyUqfarZLpHaSLJVUCwplbaVrQvKxbrEEEYnJWKeHcAGyoAVqKgW/pub?gid=119992017&single=true&output=csv'
_ggxardcom = r'http://www.ggxrd.com/pg2/usage_rate_view.php'

def get_web_csv(filename = 'local_data', link = _published_csv):
    """load a csv file from the web like a published google sheet"""
    with open(filename+'.csv', 'wb') as csvfile:
        source = urllib.request.urlopen(link)
        csvfile.write(source.read())    #_pp.pprint(csv_file)

def data_from_ggxrdcom():
    """Read date from ggxard.com and returns a dictionary with {date: today, character1 : data1, character2 : date2}"""
    character_dic = {'datetime': str(date.today())}

    with urllib.request.urlopen(_ggxardcom) as src:
        soup = BS(src.read().decode('utf-8'), 'html.parser')
        ul = soup.find('ul')
        """
        This "：" (from the html sourc) is not this ":" (the keyboard colon)
        """
        for li in ul.find_all('li'):
            character, value = li.text[1:].split("：")
            character = translate_name(character)
            character_dic[character] = value

    #print(list(character_dic.keys()))
    return character_dic

def ggxrdcom_to_csv(filename = 'ggxrdcom'):
    """loads data from ggxrd.com and appends it to a existing file"""
    dic = data_from_ggxrdcom()
    try:
        data_format = pd.read_csv(filename+'.csv')
        data_format = data_format.append(dic, ignore_index=True)
        data_format.to_csv(filename+'.csv', index=False)
    except:
        raise

def update_to_sheet_google(filename):
    worksheet = googlesheet.client.open("character_data").worksheet("ggxrd_com")

    try:
        df = pd.read_csv(filename + '.csv')
        print(len(df.columns), len(df.index))
        for col in range(len(df.columns)):
            worksheet.update_cell(1,col+1, df.columns[col])
            for row in range(len(df.index)):
                worksheet.update_cell(row+2,col+1,df.iat[row,col])
    except:
        raise

def translate_name(jp_name):
    """returns the corresponding english name for a given japanese name of a guilty gear character"""
    return translation.translation_dic.get(jp_name)

if __name__=="__main__":
    get_web_csv(link = _published_csv)
    get_web_csv(filename='ggxrd_com', link=_ggxrdcom_csv)
    ggxrdcom_to_csv()
    update_to_sheet_google(filename="ggxrdcom")