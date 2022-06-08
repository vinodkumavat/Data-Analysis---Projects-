import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from sympy import intervals

plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

index = count()

def animator(i):
    data = pd.read_csv('data.csv')
    x = data['x_value']
    y_1 = data['total_1']
    y_2 = data['total_2']

    plt.cla()
    plt.plot(x, y_1, label = 'Channel_1')
    plt.plot(x, y_2, label = 'Channel_2')
    
    plt.legend(loc = 'upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animator, interval = 1000)

plt.show()