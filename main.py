#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""display guilty gear characters play stats by day in graph"""
import csv, colour, datetime
import plotly.graph_objects as go
import pandas as pd
from os.path import sep as sep
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

def save_graph(ply_figure, filename, subfolder):
    """Saves a plotly graphic object as filename in subfolder as an html and png"""
    ply_figure.write_html(subfolder+ sep + filename + ".html")
    with open(subfolder + sep + filename + ".png", "wb") as f:
        f.write(ply_figure.to_image(format="png", engine="kaleido", width=1920, height=1080))


def generate_h_graph(data_format, characters, percentage=True, colour_coding='dft'):
    """generate horizontal graph with different colours

        data_format = a prepared array return by get_plotly_data() as the first return value
        characters =  a perpared list of characters returned by get_plotly_data() as the second return value
        percentage = a boolean, that tells plotly to display characters appearance as percentage of all, i.e. 13% Baiken
        instead of 6 Baiken
        color_coding = dlt: plotly autocolors, css1 = my choice of css colors, rog = red on gray -> Baiken is colored salmon
        and all other characters are gray.
        """

    if colour_coding == "css1":
        colours = colour.css1()
        colour_coding_str = 'unique_colours'
    elif colour_coding == "rog":
        colours = colour.red_on_gray()
        colour_coding_str = 'red_on_gray'
    else:
        colours = colour.plt_colour()
        colour_coding_str = 'plt_colours'

    fig = go.Figure()
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

    filename = "generate_h_graph_" + colour_coding_str + "_"+ str(percentage)
    save_graph(fig, filename, 'docs')


def generate_v_graph(data_format, characters, percentage=True, colour_coding='dft'):
    """generate vertical graph with different colours

    data_format = a prepared array return by get_plotly_data() as the first return value
    characters =  a perpared list of characters returned by get_plotly_data() as the second return value
    percentage = a boolean, that tells plotly to display characters appearance as percentage of all, i.e. 13% Baiken
    instead of 6 Baiken
    color_coding = dft: plotly autocolors, css1 = my choice of css colors, rog = red on gray -> Baiken is colored salmon
    and all other characters are gray.
    """
    fig = go.Figure()
    if colour_coding == "css1":
        colours = colour.css1()
        colour_coding_str = 'unique_colours'
    elif colour_coding == "rog":
        colours = colour.red_on_gray()
        colour_coding_str = 'red_on_gray'
    else:
        colours = colour.plt_colour()
        colour_coding_str = 'plt_colours'

    print(len(colours), colours)

    for i, charsi in enumerate(characters):
        fig.add_trace(go.Bar(
            y=data_format[charsi],
            x=data_format['date'],
            orientation='v',
            name=charsi,
            text=charsi,
            textposition='auto',
            marker_color=colours[i],
            hoverinfo="name+x",
        ))

    fig.update_layout(barmode='stack', title_text='Character Usage', xaxis_type='category')
    if percentage: fig.update_layout(barnorm="percent", title_text='Character Usage in %')

    filename = "generate_v_graph_" + colour_coding_str + "_"+ str(percentage)
    save_graph(fig, filename, 'docs')

if __name__ == "__main__":
    d, c = get_plotly_data()

    #percentage graphs
    generate_h_graph(d, c, True, 'rog')
    generate_h_graph(d, c, True, 'css1')
    generate_h_graph(d, c, True, 'dft')

    generate_v_graph(d, c, True, 'rog')
    generate_v_graph(d, c, True, 'css1')
    generate_v_graph(d, c, True, 'dft')

    #integer graphs

    generate_h_graph(d, c, False, 'rog')
    generate_h_graph(d, c, False, 'css1')
    generate_h_graph(d, c, False, 'dft')

    generate_v_graph(d, c, False, 'rog')
    generate_v_graph(d, c, False, 'css1')
    generate_v_graph(d, c, False, 'dft')

