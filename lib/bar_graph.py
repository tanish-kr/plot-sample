# -*- encoding: utf-8 -*-
import json
import urllib.request
import matplotlib as mpl
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://gist.githubusercontent.com/tatsu07/f1bc747e344b873bb836/raw/e650ed44f538a3f2b271c298bc4a1b98af4ba7f1/2015_Annual_income.json'

response = urllib.request.urlopen(url)
income_data = pd.read_json(response.read().decode('utf-8'))

mpl.rcParams['font.family']='MS Gothic'

# Tで行列を入れ替える
income_data.T.plot(kind='bar', color=['g','r','b'])

plt.title('年代別 年収')
plt.ylabel("年収")
plt.xlabel("年代")

# 余白設定
plt.gcf().subplots_adjust(bottom=0.15)

plt.savefig('income_bar.png')
