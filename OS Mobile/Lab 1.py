import numpy as np
import matplotlib.pyplot as plt
import prettytable as pretty


def MakeNewAx(figure, pos, name):
    """Crates a graphic and presets it
    :return Object of created graphic
    """
    ax = figure.add_subplot(1, 2, pos)
    ax.set_title(name)
    ax.set_xlabel("Вісь X")
    ax.set_ylabel("Вісь Y")
    return ax


def FloatValueEnter(msg):
    """Enter a value
    and check if the value entered is float

    msg - a message of entering

    :return float value
    """
    while True:
        floatVal = input(msg)
        # check whether the entered value is float
        try:
            taker = float(floatVal)
        except ValueError:
            continue
        else:
            return float(floatVal)


def PrintTable():
    """The function prints the table of x f(x) into console"""
    table = pretty.PrettyTable(['Значення X', 'Значення x / cos(x)'])
    for x in np.arange(x_start, x_end + step, step):
        if x > x_end:
            x = x_end
        table.add_row(['{:.5f}'.format(x),
                       '{:.5f}'.format(x / np.cos(x))])
    print(table)


# Entering start, end x and the tabulation step
x_start = FloatValueEnter('Введіть початкову точку Х: ')
x_end = FloatValueEnter('Введіть кінцеву точку X: ')
if x_end < x_start:
    x_start, x_end = x_end, x_start
step = np.abs(FloatValueEnter('Введіть крок табуляції: '))
if step == 0:
    step = (x_end - x_start) / 10

# Printing the x f(x) table
PrintTable()

# Creating a field to place graphics on
plt.style.use('seaborn-whitegrid')
figure = plt.figure(figsize=(12, 5))

# Main graphic creating
mainAx = MakeNewAx(figure, 1, 'Графік')
mainAx.set_xlim(x_start, x_end)
mainAx.set_ylim(-4 * np.abs(x_start), 4 * x_end)

array_x = np.linspace(x_start, x_end, 10000)  # List of x values [x_start, x_end]
array_y = np.linspace(x_start, x_end, 10000)  # List of x/cos(x) values

zero_points = []  # List of breakpoints
for i in range(len(array_x)):
    if np.abs(np.cos(array_x[i])) < 0.001:  # If a breakpoint is found
        zero_points.append(array_x[i])  # Add the breakpoint to the list
        array_x[i] = np.nan
    else:
        array_y[i] = array_x[i] / np.cos(array_x[i])

# Printing the main graphic on the field (figure)
mainAx.plot(array_x, array_y, color='black', label='y = x / cos (x)')
mainAx.legend(loc='upper right')

# Printing asymptotes
for x in zero_points:
    mainAx.axvline(x=x, linestyle='--', label='')

# Creating extra graphic for special points
extraAx = MakeNewAx(figure, 2, 'Особливі точки')
extraAx.set_xlim(x_start, x_end)
extraAx.set_ylim(-4 * np.abs(x_start), 4 * x_end)

# Finding max values of x / cos(x) on the interval
# by indexing operation
high = np.where((array_y[1:-1] < array_y[0:-2]) * \
                (array_y[1:-1] < array_y[2:]))[0]
# Finding min values of x / cos(x) on the interval
# by indexing operation
low = np.where((array_y[1:-1] > array_y[0:-2]) * \
               (array_y[1:-1] > array_y[2:]))[0]

# Printing x / cos(x) graphic
extraAx.plot(array_x, array_y, color='black')
# Printing min and max values on the extra graphic
extraAx.scatter(array_x[high], array_y[high],
                marker='o', label='Точки локального максимуму')
extraAx.scatter(array_x[low], array_y[low],
                marker='o', label='Точки локального мінімуму')
# Since the function only has one point of crossing
# Ox and Oy - print the point without extra operations
extraAx.scatter(0, 0, marker='o', color='black',
                label='Єдина точка перетину з Ox та Oy')

extraAx.legend(loc='upper right')
plt.show()
