#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""load character data from my web source or local and provide into a file"""
import urllib.request
import pandas as pd
import ggxrdcom as gg
import googlesheet

_published_csv = r'https://docs.google.com/spreadsheets/d/e/2PACX-1vS7VtGA2e06j226OnbwcMXzk2z1KyUqfarZLpHaSLJVUCwplbaVrQvKxbrEEEYnJWKeHcAGyoAVqKgW/pub?gid=1914483541&single=true&output=csv'
_ggxrdcom_csv = r'https://docs.google.com/spreadsheets/d/e/2PACX-1vS7VtGA2e06j226OnbwcMXzk2z1KyUqfarZLpHaSLJVUCwplbaVrQvKxbrEEEYnJWKeHcAGyoAVqKgW/pub?gid=119992017&single=true&output=csv'


def get_web_csv(filename='local_data', link=_published_csv):
    """load a csv file from the web like a published google sheet"""
    with open(filename + '.csv', 'wb') as csvfile:
        source = urllib.request.urlopen(link)
        csvfile.write(source.read())  # _pp.pprint(csv_file)


def update_to_sheet_google(filename):
    """slow version to update all cells cell by cell"""
    worksheet = googlesheet.client.open("character_data").worksheet("ggxrd_com")

    try:
        df = pd.read_csv(filename + '.csv')
        for col in range(len(df.columns)):
            worksheet.update_cell(1, col + 1, df.columns[col])
            for row in range(len(df.index)):
                worksheet.update_cell(row + 2, col + 1, df.iat[row, col])
    except:
        raise


def update_google_sheet(filename):
    """another method to update the googlesheet"""
    worksheet = googlesheet.client.open("character_data").worksheet("ggxrd_com")

    try:
        print("Reading local file {}.csv".format(filename))
        df = pd.read_csv(filename + '.csv')
        print("Updating worksheet...")
        worksheet.update([df.columns.values.tolist()] + df.values.tolist())
        print("Updating worksheet...done")
    except:
        raise


if __name__ == "__main__":
    get_web_csv(link=_published_csv)
    get_web_csv(filename='google_ggxrd_com', link=_ggxrdcom_csv)
    gg.ggxrdcom_to_csv()
    update_to_sheet_google(filename="ggxrdcom")
