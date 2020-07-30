#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""load character data from my web source or local and provide into a file"""
import urllib.request, pprint
from bs4 import BeautifulSoup as BS

_published_csv = r'https://docs.google.com/spreadsheets/d/e/2PACX-1vS7VtGA2e06j226OnbwcMXzk2z1KyUqfarZLpHaSLJVUCwplbaVrQvKxbrEEEYnJWKeHcAGyoAVqKgW/pub?gid=1914483541&single=true&output=csv'
_ggxrdcom_csv = r'https://docs.google.com/spreadsheets/d/e/2PACX-1vS7VtGA2e06j226OnbwcMXzk2z1KyUqfarZLpHaSLJVUCwplbaVrQvKxbrEEEYnJWKeHcAGyoAVqKgW/pub?gid=119992017&single=true&output=csv'
_ggxardcom = r'http://www.ggxrd.com/pg2/usage_rate_view.php'
_test = "Kum,Elphelt,Ram,Raven,Sin,Chipp,Millia,Anwser,Zato,Axl,Faust,Bedman,Jacko"
_translation_dic = {    'ソル=バッドガイ' : 'Sol',
                        'カイ=キスク' : 'Ky',
                        'スレイヤー' : 'Slayer',
                        'ジョニー' : 'Johnny',
                        '梅喧' : 'Baiken',
                        'ポチョムキン' : 'Potemkin',
                        'メイ' : 'May',
                        'レオ=ホワイトファング' : 'Leo',
                        'シン=キスク' : 'Sin',
                        'エルフェルト=ヴァレンタイン' : 'Elphelt',
                        'ディズィー' : 'Dizzy',
                        'ヴェノム' : 'Venom',
                        'イノ' : 'INo',
                        '蔵土縁紗夢' : 'Jam'
                        'レイヴン' :
                        'ファウスト' :
                        'ミリア=レイジ' :
                        'アクセル=ロウ' :
                        'ラムレザル=ヴァレンタイン' :
                        'チップ=ザナフ' :
                        'ザトー=ONE' :
                        'アンサー' :
                        'ベッドマン' :
                        '琴 慧弦' :
                        'ジャック・オー' :
                        }
def get_web_csv(filename = 'local_data', link = _published_csv):
    """load a csv file from the web like a published google sheet"""
    with open(filename+'.csv', 'wb') as csv:
        source = urllib.request.urlopen(link)
        csv.write(source.read())    #_pp.pprint(csv_file)

def data_from_ggxrdcom():
    with urllib.request.urlopen(_ggxardcom) as src:
        soup = BS(src.read().decode('utf-8'), 'html.parser')
        list = soup.find('ul')

        """
        This "：" (from the html sourc) is not this ":" (the keyboard colon)
        """
        character_dic = {}
        for el in list.find_all('li'):
            character, value = el.text[1:].split("：")
            character_dic[character] = value
            print("'"+character+"' :")

def translate_name(jp_name):

    return english_name
if __name__=="__main__":
    #get_web_csv(link = _published_csv)
    #get_web_csv(filename='ggxrdcom', link=_ggxrdcom_csv)
    data_from_ggxrdcom()