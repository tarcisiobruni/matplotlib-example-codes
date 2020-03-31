import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.use('seaborn')


def animate(i):
    data = pd.read_csv('data-live-time-series.g.csv').tail(90)
    data['date_value'] = pd.to_datetime(data['date_value'])
    data.sort_values('date_value', inplace=True)
    
    price_date = data['date_value']
    dateMark = data.loc[price_date.index[-1]].at['date_value']
    
    price = data['number_value']
    priceMark = data.loc[price.index[-1]].at['number_value']

    plt.cla()
    
    plt.plot(dateMark,priceMark,marker="X") ## Useful to plot some marker 
    plt.plot_date(price_date,price,linestyle='solid',label='Indicator',marker=None)

    plt.axhline(y=70,color='#ffd700')
    plt.axhline(y=30,color='#f45454')
    plt.gcf().autofmt_xdate()

    plt.legend(loc='upper left')
    plt.tight_layout()

ani = FuncAnimation(plt.gcf(),animate, interval = 250)

plt.tight_layout()

plt.show()

