import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# Constants
y = 10  # antal punkter i yled
n = 20  # time steps
duration = 1
period = 4

y_list = np.linspace(0, 1, y)
L = 1      # heat transfer


def psi(x, t):
    a = (np.pi * (x + t)) / 2
    c = a < 4 * np.pi
    a = a * c
    c = a > 2 *np.pi

    return np.sin(c*a)**2


temp_col = np.empty(0)
y_col = np.empty(0)
t_col = np.empty(0)

count = 0
for time in np.linspace(period/2, period*2, n):
    x = y_list
    temp = psi( x, time)

    time_list = np.full(y, count)

    temp_col = np.append(temp_col, temp)
    y_col = np.append(y_col, x)
    t_col = np.append(t_col, time_list)
    count = count + 1


data = {'time': t_col, 'y': y_col, 'temp': temp_col, }
df = pd.DataFrame.from_dict(data)
df['y'] = df['y']*0.4

df.loc[df['temp'] > 0.3, 'temp'] = 0.3
df['temp'] = df['temp'] / 0.3
df['time'] = df['time'] / n * duration

# df.plot()
# plt.show()
df.to_csv('double_sinus.txt', index = False, header = False)

dfg = df.groupby(['time'])

for i, data in dfg:
    print(i, data.head())
    data.plot(y='temp', x='y')
    plt.suptitle(i)
    plt.ylim(0, 1)
    plt.show()


