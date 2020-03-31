import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.use('seaborn')

index = count()

x_vals = []
y_vals = []

def animate(i):
    data = pd.read_csv('data-live-chart.g.csv')
    x = data['x_value']
    y1 = data['total_1']
    y2 = data['total_2']

    plt.cla()
    plt.plot(x, y1, label='Channel 1')
    plt.plot(x, y2, label='Channel 2')

    plt.legend(loc='upper left')
    plt.tight_layout()

    # x_vals.append(next(index))
    # y_vals.append(random.randint(0,5))

    # plt.plot(x_vals,y_vals) 

ani = FuncAnimation(plt.gcf(),animate, interval = 1000)


plt.tight_layout()

plt.show()

