#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""display guilty gear characters play stats by day in graph"""
from itertools import cycle
from os.path import sep as sep

import pandas as pd
import plotly.graph_objects as go

import colour


def get_plotly_data():
    """reads csv from a the local file local_data.csv into a data_format and characters."""
    try:
        data_format = pd.read_csv("local_data.csv")
        """ # plotly can not skip empty dates and cant format category for fuck all reason... we work with string dates
        data_format['date'] = data_format['date'] + " " + data_format['time']
        #data_format['date'] = pd.to_datetime(data_format['date'].astype('datetime64[ns]'))
        """
        del data_format["time"]
        # print(data_format['date'])
        characters = data_format.keys()[1:].sort_values()
        return data_format, characters

    except:
        raise


def save_graph(ply_figure, filename, subfolder, width=1920, height=1080):
    """Saves a plotly graphic object as filename in subfolder as an html and png"""

    ply_figure.write_html(subfolder + sep + filename + ".html")
    with open(subfolder + sep + filename + ".png", "wb") as f:
        f.write(ply_figure.to_image(format="png", engine="kaleido", width=width, height=height))


def graph_bar_text(charsi, data_format, percentage=False):
    """the text field of a trace has to be a string or string list, therefore "dynamic information has to be
    precompiled. We create a list, that is the string representation of Value - Character per character
    example:  ['2.4% Anwser', '0.0% Anwser', '2.8% Anwser', '0.0% Anwser', '0.0% Anwser'].
    This is implicit sorted by day from earliest to latest.
    """
    ziplist = []
    for j, z in enumerate(list(zip(cycle([charsi]), data_format[charsi]))):
        daily_sum = data_format.sum(axis=1)
        if percentage:
            f = "{:.1f}".format(z[1] / daily_sum[j] * 100) + r'%'
        else:
            f = "{:.0f}".format(z[1])
        ziplist.append(f + " " + z[0])

    return ziplist


def generate_h_graph(data_format, characters, percentage=True, colour_coding='dft'):
    """generate horizontal graph with different colours

        data_format = a prepared array return by get_plotly_data() as the first return value
        characters =  a perpared list of characters returned by get_plotly_data() as the second return value
        percentage = a boolean, that tells plotly to display characters appearance as percentage of all, i.e. 13% Baiken
        instead of 6 Baiken
        color_coding = dlt: plotly autocolors, css1 = my choice of css colors, rog = red on gray -> Baiken is colored salmon
        and all other characters are gray.
        """

    #Choose colour coding of the graphs
    if colour_coding == "css1":
        colours = colour.css1()
        colour_coding_str = 'unique_colours'
    elif colour_coding == "rog":
        colours = colour.red_on_gray()
        colour_coding_str = 'red_on_gray'
    else:
        colours = colour.plt_colour()
        colour_coding_str = 'plt_colours'


    #We make one plotly figure and add trace per character.
    #A trace consist of the characters pick rate per day
    fig = go.Figure()
    for i, charsi in enumerate(characters):
        ziplist = graph_bar_text(charsi, data_format, percentage)

        fig.add_trace(go.Bar(
            y=data_format['date'],
            x=data_format[charsi],
            orientation='h',
            name=charsi,
            text=ziplist,
            textposition='inside',
            marker_color=colours[i],
            hoverinfo="name+x",
        ))

    #barmode = stack means, that data from each character is stacked on eachother per day
    fig.update_layout(barmode='stack', title_text='Character Usage', yaxis_type='category',
                      yaxis_categoryorder='category ascending',
                      xaxis_title="Sample Size", yaxis_title="Sample Dates", legend_title="Characters",
                      )

    #barnomr = percent changes display from absolute values to percentage
    if percentage:
        fig.update_layout(barnorm="percent", title_text='Character Usage in %', xaxis_title="Percentage of Sample Size")


    filename = "generate_h_graph_" + colour_coding_str + "_" + str(percentage)
    height = len(data_format['date']) * 220 #to stop plotly from compressing the visuals of the data to much
    save_graph(fig, filename, 'docs', height=height)


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
        ziplist = graph_bar_text(charsi, data_format, percentage)

        fig.add_trace(go.Bar(
            y=data_format[charsi],
            x=data_format['date'],
            orientation='v',
            name=charsi,
            text=ziplist,
            textposition='inside',
            marker_color=colours[i],
            hoverinfo="name+y",
        ))

    fig.update_layout(barmode='stack', title_text='Character Usage', xaxis_type='category',
                      xaxis_categoryorder='category ascending',
                      yaxis_title="Sample Size", xaxis_title="Sample Dates", legend_title="Characters",
                      )

    if percentage:
        fig.update_layout(barnorm="percent", title_text='Character Usage in %', yaxis_title="Percentage of Sample Size")

    filename = "generate_v_graph_" + colour_coding_str + "_" + str(percentage)
    width = len(data_format['date']) * 300
    save_graph(fig, filename, 'docs', width)


def test_stub(d, c):
    generate_h_graph(d, c, eval("True"), "rog")
    generate_v_graph(d, c, eval("True"), "rog")


if __name__ == "__main__":

    # data_preparation.get_web_csv()

    d, c = get_plotly_data()
    col_coding = ["rog", "css1", "dft"]
    display_in_percentage = ["True", "False"]

    for mode in display_in_percentage:
        for percentage, col in zip(cycle([mode]), col_coding):
            print("Rendering: " + percentage, col)
            generate_h_graph(d, c, eval(percentage), col)
            print("horizontal - done")
            generate_v_graph(d, c, eval(percentage), col)
            print("vertical - done")

    # test_stub(d,c)
