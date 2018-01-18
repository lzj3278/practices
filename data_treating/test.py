# -*- coding:utf-8 -*-
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
import requests
import json

URL = 'https://api.github.com/search/repositories?q=language:python&sort=star'
r = requests.get(URL)
response_dicts = r.json()
# print(json.dumps(response_dicts, indent=4))
repo_dicts = response_dicts['items']
names, starts_desc = [], []
for item in repo_dicts:
    names.append(item['name'])
    dic_list = {
        'value': item['stargazers_count'],
        'label': item['description'],
        'xlink': item['html_url']
    }
    starts_desc.append(dic_list)
print starts_desc
# names = ['django', 'flask', 'http']
# starts_desc = [
#     {'value': 1111, 'label': '22222'},
#     {'value': 1113, 'label': '22222'},
#     {'value': 1112, 'label': '22222'}
# ]

my_style = LS('#333366', base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most_Starts python projects on GitHub'
chart.x_labels = names
chart.add('', starts_desc)
chart.render_to_file('python_start.svg')
