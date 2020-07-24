#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""display guilty gear characters play stats by day in graph"""
import csv
import plotly.express as px
import pandas as pd
published_csv = r'https://docs.google.com/spreadsheets/d/e/2PACX-1vS7VtGA2e06j226OnbwcMXzk2z1KyUqfarZLpHaSLJVUCwplbaVrQvKxbrEEEYnJWKeHcAGyoAVqKgW/pub?gid=1914483541&single=true&output=csv'

def get_csv():
    """depreciated"""
    with open("local_data.csv",newline='',) as csvfile:
        reader = csv.DictReader(csvfile, dialect='excel')
        for dic in reader:
            dic.pop('daily sum')
            if "character sum" == dic.get("time"):
                print("skip")
                break
            print(dic)

def get_csv_via_panda():
    try:
        data_format = pd.read_csv("local_data.csv")
        data_format = data_format[:-1]
        del data_format["daily sum"]
        print(data_format.keys()[2:])
        chars = data_format.keys()[3:-1]

        fig1 = px.bar(data_format, x=chars, y="date", orientation='h', hover_data = { 'date' : False}, title="Character Usage in %")
        fig1.update_layout( barnorm = "percent")
        fig1.show()

        fig2 = px.bar(data_format, x=chars, y="date", orientation='h', hover_name="name",hover_data = { 'date' : False}, title="Charater Usage")
        fig2.update_layout( hover_data="test")
        fig2.show()
    except:
        raise

if __name__ == "__main__":
    get_csv_via_panda()