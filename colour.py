#!/usr/bin/python3
# -*- coding: utf-8 -*-

_c = 25
css1 = ['DarkBlue','DarkGray','DarkKhaki', 'DarkOrange', 'DarkSalmon',
                'DarkSlateGray', 'DarkViolet', 'DimGray', 'Firebrick', 'Fuchsia',
                'Gold', 'DeepPink', 'Green', 'Cyan', 'Orchid',
                'Tomato', 'NavajoWhite', 'CadetBlue', 'DarkOliveGreen','PaleVioletRed',
                'YellowGreen','DarkTurquoise','GoldenRod', 'LightSeaGreen','LightSeaGreen']

class character_colours():
    sol = 0xD45B47
    el = 0xFDF3BD
    kum = 0x393750
    ky = 0x0F0D42
    ram = 0x0F0D42
    raven = 0x3B2926
    sin = 0x5D6573
    johnny = 0x1B1518
    may = 0xFF6A00
    leo = 0x00693F
    chipp = 0x24B613
    millia = 0xFCF114
    baiken = 0xF97580
    answer = 0x063501
    zato = 0x000000
    potemkin = 0xC0B09F
    ino = 0xF90014
    slayer = 0x9C6542
    venom = 0x562A0D
    axl = 0x441654
    dizzy = 0x7AA9CC
    faust = 0xB8ED1A
    bedman = 0xEF377B
    jacko = 0xED9A00
    jam = 0xFF614C
"""
class mathplotlib_colour():
    import matplotlib, random

    hex_colors_dic = {}
    rgb_colors_dic = {}
    hex_colors_only = []
    for name, hex in matplotlib.colors.cnames.items():
        hex_colors_only.append(hex)
        hex_colors_dic[name] = hex
        rgb_colors_dic[name] = matplotlib.colors.to_rgb(hex)

    print(hex_colors_only)

    # getting random color from list of hex colors

    print(random.choice(hex_colors_only))
"""