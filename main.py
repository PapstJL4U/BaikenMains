#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""display guilty gear characters play stats by day in graph"""
import csv, colour, datetime
import plotly.graph_objects as go
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

def get_plotly_data():
    try:
        data_format = pd.read_csv("local_data.csv")
        data_format = data_format[:-1]
        del data_format["daily sum"]
        data_format['date'] = data_format['date'] + " " + data_format['time']
        data_format['date'] = data_format['date'].astype('datetime64[ns]')
        del data_format["time"]

        characters = data_format.keys()[1:].sort_values()
        return data_format,characters

    except:
        raise

def generate_h_graph_red_on_gray(data_format, characters, percentage=True):
    """generate a character usage graph, where Baikens data is salmon colour and everything else gray"""
    colours = colour.red_on_gray()
    fig = go.Figure()
    for i, charsi in enumerate(characters):
        fig.add_trace(go.Bar(
            y=data_format['date'],
            x=data_format[charsi],
            orientation='h',
            name=charsi,
            marker_color=colours[i],
            hoverinfo="name+x",
        ))
    fig.update_layout(barmode='stack', title_text='Character Usage', yaxis_type='category')
    if percentage: fig.update_layout(barnorm="percent", title_text='Character Usage in %')
    fig.show()

def generate_h_graph_unique_colour(data_format, characters, percentage=True):
    "generate horizontal graph with plotly default colours"
    fig = go.Figure()
    colours = colour.css1()
    for i, charsi in enumerate(characters):
        fig.add_trace(go.Bar(
            y=data_format['date'],
            x=data_format[charsi],
            orientation='h',
            name=charsi,
            text=charsi,
            textposition='auto',
            marker_color=colours[i],
            hoverinfo="name+x",
        ))
    fig.update_layout(barmode='stack', title_text='Character Usage in %',yaxis_type='category')
    if percentage: fig.update_layout(barnorm="percent")
    fig.show()
    fig.write_html("exports/generate_h_graph_unique_colour_"+str(percentage)+".html")
    with open("exports/generate_h_graph_unique_colour_"+str(percentage)+".png", "wb") as f:
        f.write(fig.to_image(format="png", engine="kaleido", width=1920, height=1080))

def generate_h_graph(data_format, characters, percentage=True):
    "generate horizontal graph with plotly default colours"
    fig = go.Figure()
    for i, charsi in enumerate(characters):
        fig.add_trace(go.Bar(
            y=data_format['date'],
            x=data_format[charsi],
            orientation='h',
            name=charsi,
            hoverinfo="name+x",
        ))
    fig.update_layout(barmode='stack', title_text='Character Usage in %',yaxis_type='category')
    if percentage: fig.update_layout(barnorm="percent")
    fig.show()

def generate_v_graph(data_format, characters, percentage=True):
    "generate horizontal graph with plotly default colours"
    fig = go.Figure()
    colours = colour.red_on_gray()
    print(colours)
    for i, charsi in enumerate(characters):
        fig.add_trace(go.Bar(
            y=data_format[charsi],
            x=data_format['date'],
            orientation='v',
            name=charsi,
            marker_color=colours[i],
            hoverinfo="name+x",
        ))
    fig.update_layout(barmode='stack', title_text='Character Usage', xaxis_type='category')
    if percentage: fig.update_layout(barnorm="percent", title_text='Character Usage in %')
    fig.show()

if __name__ == "__main__":
    d, c = get_plotly_data()
    #generate_h_graph(d,c)
    #generate_h_graph(d,c,False)
    #generate_h_graph_red_on_gray(d,c)
    #generate_h_graph_red_on_gray(d,c, False)
    #generate_v_graph(d,c)
    generate_h_graph_unique_colour(d,c)