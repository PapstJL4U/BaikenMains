#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""display guilty gear characters play stats by day in graph"""
import csv, colour, data_preparation
import plotly.graph_objects as go
import pandas as pd
from os.path import sep as sep
from itertools import cycle
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
    """reads csv from a the local file local_data.csv into a data_format and characters."""
    try:
        data_format = pd.read_csv("local_data.csv")

        """ # plotly can not skip empty dates and cant format category for fuck all reason... we work with string dates....
        data_format['date'] = data_format['date'] + " " + data_format['time']
        #data_format['date'] = pd.to_datetime(data_format['date'].astype('datetime64[ns]'))
        """
        del data_format["time"]
        #print(data_format['date'])
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

        ziplist = []
        for z in list(zip(cycle([charsi]), data_format[charsi])):
            f = "{:.0f}".format(z[1])
            ziplist.append(f + " " + z[0])

        fig.add_trace(go.Bar(
            y=data_format['date'],
            x=data_format[charsi],
            orientation='h',
            name=charsi,
            text=ziplist,
            textposition='auto',
            marker_color=colours[i],
            hoverinfo="name+x",
        ))

    fig.update_layout(barmode='stack', title_text='Character Usage', yaxis_type='category',
                      yaxis_categoryorder='category ascending',
                      xaxis_title="Sample Size", yaxis_title="Sample Dates", legend_title="Characters",
                      )

    if percentage: fig.update_layout(barnorm="percent", title_text='Character Usage in %', xaxis_title="Percentage of Sample Size")

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

    for i, charsi in enumerate(characters):

        ziplist = []
        for z in list(zip(cycle([charsi]), data_format[charsi])):
            f = "{:.0f}".format(z[1])
            ziplist.append(f +" " + z[0])

        fig.add_trace(go.Bar(
            y=data_format[charsi],
            x=data_format['date'],
            orientation='v',
            name=charsi,
            text= ziplist,
            textposition='inside',
            marker_color=colours[i],
            hoverinfo="name+y",
        ))

    fig.update_layout(barmode='stack', title_text='Character Usage', xaxis_type='category',
                      xaxis_categoryorder='category ascending',
                      yaxis_title="Sample Size", xaxis_title="Sample Dates", legend_title="Characters",
                      )

    if percentage: fig.update_layout(barnorm="percent", title_text='Character Usage in %', yaxis_title="Percentage of Sample Size")

    filename = "generate_v_graph_" + colour_coding_str + "_"+ str(percentage)
    save_graph(fig, filename, 'docs')

if __name__ == "__main__":

    #data_preparation.get_web_csv()

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
