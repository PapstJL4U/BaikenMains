#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""load character usage rate in % from ggxrd.com"""
import urllib.request, translation
import pandas as pd
from datetime import date
from bs4 import BeautifulSoup as BS

_ggxardcom = r'http://www.ggxrd.com/pg2/usage_rate_view.php'

def translate_name(jp_name):
    """returns the corresponding english name for a given japanese name of a guilty gear character"""
    return translation.translation_dic.get(jp_name)

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

    return character_dic

def ggxrdcom_to_csv(filename='ggxrdcom'):
    """loads data from ggxrd.com and appends it to a existing file"""
    dic = data_from_ggxrdcom()
    try:
        data_format = pd.read_csv(filename + '.csv')
        data_format = data_format.append(dic, ignore_index=True)
        data_format.to_csv(filename + '.csv', index=False)
    except:
        raise

if __name__ == "__main__":
    file = 'ggxrdcom'
    print("Getting data from: "+_ggxardcom)
    ggxrdcom_to_csv(file)
    print("data appened to {}.csv".format(file))