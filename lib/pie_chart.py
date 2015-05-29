# -*- encoding: utf-8 -*-
import json
import urllib.request
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

url = 'https://gist.githubusercontent.com/tatsu07/f1bc747e344b873bb836/raw/e650ed44f538a3f2b271c298bc4a1b98af4ba7f1/2015_Annual_income.json'

response = urllib.request.urlopen(url)
income_data = pd.read_json(response.read().decode('utf-8'))

colors = ['#F5BCA9', '#F5F6CE', '#D0F5A9', '#A9F5D0', '#A9A9F5', '#E2A9F3', '#F6CEE3', \
        '#F7BE81', '#F4FA58', '#81F781']

mpl.rcParams['font.family']='MS Gothic'
income_data.T['avg'].plot(kind='pie', colors=colors)

plt.title('年代別 年収の割合')

plt.gca().legend(bbox_to_anchor=(0.5, 0.05), loc="upper center", ncol=4)
plt.gcf().subplots_adjust(bottom=0.2)

plt.savefig('income_pie_chart.png')
