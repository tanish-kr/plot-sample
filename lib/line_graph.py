# -*- encoding: utf-8 -*-
import json
import datetime
import urllib.request
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

url = 'https://gist.githubusercontent.com/tatsu07/304b6e8068313a1744d5/raw/7c22672af63f548caaca314c9135461099a970e8/20150529_JP_Temperature.json'
response = urllib.request.urlopen(url)
temperature_data = json.loads(response.read().decode('utf-8'))

# フォント指定
mpl.rcParams['font.family']='MS Gothic'

fig = plt.figure()

# キャンパス追加
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)

ax1.set_title("各地の気温")

# x軸日付設定
days = mdates.AutoDateLocator()
daysFmt = mdates.DateFormatter('%m/%d')
ax1.xaxis.set_major_locator(days)
ax1.xaxis.set_major_formatter(daysFmt)
ax2.xaxis.set_major_locator(days)
ax2.xaxis.set_major_formatter(daysFmt)

# ラベル設定
# ax1.set_xlabel("date")
ax1.set_ylabel("最高気温")
ax2.set_xlabel("date")
ax2.set_ylabel("最低気温")

for area,data in temperature_data.items():
    date_list = []
    highest_temperature = []
    minimum_temperature = []

    for temperature in data:
        date_list.append(datetime.datetime.strptime(temperature['date'], '%Y-%m-%d'))
        highest_temperature.append(temperature['max'])
        minimum_temperature.append(temperature['min'])

    ax1.plot(date_list, highest_temperature, label=area)
    # ax1.legend(bbox_to_anchor=(1.05, 1), loc="upper right")
    ax1.grid()
    ax2.plot(date_list, minimum_temperature, label=area)
    ax2.legend(bbox_to_anchor=(0.5, -0.25), loc="upper center", ncol=4)
    ax2.grid()

plt.gcf().subplots_adjust(bottom=0.2)
plt.savefig('temperature.png')
