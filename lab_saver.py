import numpy as np
import matplotlib.pyplot as plt
import os

plt.style.use('seaborn-whitegrid')


def MakeNewAx(figure, pos, name):
    ax = figure.add_subplot(1, 2, pos)
    ax.set_title(name)
    ax.set_xlabel("Вісь X")
    ax.set_ylabel("Вісь Y")
    return ax


def FloatValueEnter(msg):
    while True:
        floatVal = input(msg)
        try:
            taker = float(floatVal)
        except ValueError:
            continue
        else:
            return float(floatVal)


def PrintTable(x_start, x_end, step):
    array_x = np.linspace(x_start, x_end, int(x_end - x_start) / step)
    print("X\tf(X)")
    for x in array_x:
        print(f"{x}\t{array_x / np.cos(x)}")


x_start = FloatValueEnter('Введіть початкову точку Х: ')
x_end = FloatValueEnter('Введіть кінцеву точку X: ')
if x_end < x_start:
    x_start, x_end = x_end, x_start
step = np.abs(FloatValueEnter('Введіть крок табуляції: '))
if step == 0:
    step = (x_end - x_start) / 10

PrintTable(x_start, x_end, step)

figure = plt.figure(figsize=(10, 10))
mainAx = MakeNewAx(figure, 1, "Графік")
mainAx.set_xlim(x_start, x_end)
mainAx.set_ylim(-40, 40)

# main graphic
array_x = np.linspace(x_start, x_end, 10000)
zero_points = []
for i in range(len(array_x)):
    if np.abs(np.cos(array_x[i])) < 0.001:
        zero_points.append(array_x[i])
        array_x[i] = np.nan
mainAx.plot(array_x, array_x / np.cos(array_x), color='black')
for x in zero_points:
    mainAx.axvline(x=x, linestyle='--')
# extra graphic
plt.show()
