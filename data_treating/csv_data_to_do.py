# -*- coding:utf-8 -*-
import csv
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
from datetime import datetime

filename = 'sitka_weather_2014.csv'


def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
        seen.add(item)


seen = []
a = None


def seen_date(item):
    global a
    if a is None:
        a = item
        seen.append(item)
    else:
        if a[:7] != item[:7]:
            seen.append(item)
            a = item


with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)
    date, highs, lab_date, low = [], [], [], []
    for i in reader:
        highs.append(int(i[1]))
        low.append(int(i[3]))
        time_do = datetime.strptime(i[0], '%Y-%m-%d')
        # current_time = datetime.strftime(time_do, '%B %d %Y')
        lab_date = datetime.strftime(time_do, '%Y-%m-%d')
        date.append(lab_date)
        seen_date(lab_date)

my_style = LS('#333366', base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = -45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.show_minor_x_labels = False
# my_config.show_only_major_dots = True
# my_config.fill_between = True
chart = pygal.Line(my_config, style=my_style, dots_size=1, fill=True)
chart.title = u'weather'
chart.x_labels = date
chart.x_labels_major = seen

chart.add(u'最高温度', highs)
chart.add(u'最低温度', low)
chart.render_to_file('weather.svg')
