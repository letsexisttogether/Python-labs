import numpy as np
import matplotlib.pyplot as plt


def MakeNewAx(figure, pos, name):
    '''Функція для створення і налаштування нового графіку
    :return Об'єкт нового графіку
    '''
    ax = figure.add_subplot(1, 2, pos)
    ax.set_title(name)
    ax.set_xlabel("Вісь X")
    ax.set_ylabel("Вісь Y")
    return ax


def FloatValueEnter(msg):
    '''Функція для зчитування float числа

    msg - Повідомлення для вводу

    :return Число з комою
    '''
    while True:
        floatVal = input(msg)
        # перевірка на можливість конвертації у число
        try:
            taker = float(floatVal)
        except ValueError:
            continue
        else:
            return float(floatVal)


def PrintTable(x_start, x_end, step):
    '''Функція для виводу таблиці у консоль

    x_start - початкове значення x
    x_end - кінцеве значення x \
    step - шаг табуляції для таблиці
    '''
    array_x = np.linspace(x_start, x_end, int((x_end - x_start) / step))
    print("X\tf(X)")
    for x in array_x:
        print("{:.5f}\t{:.5f}" .format(x, x / np.cos(x)))

# Введення початкового, кінцевого x та кроку табуляції
x_start = FloatValueEnter('Введіть початкову точку Х: ')
x_end = FloatValueEnter('Введіть кінцеву точку X: ')
if x_end < x_start:
    x_start, x_end = x_end, x_start
step = np.abs(FloatValueEnter('Введіть крок табуляції: '))
if step == 0:
    step = (x_end - x_start) / 10

# Виведення таблиці значення x, f(x) на екран
PrintTable(x_start, x_end, step)

plt.style.use('seaborn-whitegrid')
# Створення поля для графіків
figure = plt.figure(figsize=(12, 5))
mainAx = MakeNewAx(figure, 1, 'Графік')
mainAx.set_xlim(x_start, x_end)
mainAx.set_ylim(-4 * np.abs(x_start), 4 * x_end)

array_x = np.linspace(x_start, x_end, 10000)    # Список значень x на заданому проміжку
array_y = np.linspace(x_start, x_end, 10000)    # Список значень функції x/cos(x)


zero_points = []    # Список для зберігання точок розриву
for i in range(len(array_x)):
    if np.abs(np.cos(array_x[i])) < 0.001:  # Якщо знайдено точку розриву
        zero_points.append(array_x[i])      # Додаємо її у відповідний список
        array_x[i] = np.nan                 # У списка X це значення = None
    else:
        array_y[i] = array_x[i] / np.cos(array_x[i])

# Виведення графіку на полі figure
mainAx.plot(array_x, array_y, color='black', label='y = x / cos (x)')
mainAx.legend(loc='upper right')

# Виведення асимптот на точках розриву
for x in zero_points:
    mainAx.axvline(x=x, linestyle='--', label='')

# Створення додаткового графіку для особливих точок
extraAx = MakeNewAx(figure, 2, 'Особливі точки')
extraAx.set_xlim(x_start, x_end)
extraAx.set_ylim(-4 * np.abs(x_start), 4 * x_end)

# Пошук максимумів функції на заданому проміжку
# за допомогою індексування
high = np.where((array_y[1:-1] < array_y[0:-2]) * \
                (array_y[1:-1] < array_y[2:]))[0]
# Пошук мінімумів функції на заданому проміжку
# за допомогою індексування
low = np.where((array_y[1:-1] > array_y[0:-2]) * \
               (array_y[1:-1] > array_y[2:]))[0]

# Виведення графіку функції
extraAx.plot(array_x, array_y, color='black')
# Виведення точок мінінмуму та максиму
extraAx.scatter(array_x[high], array_y[high], \
                marker='o', label='Точки локального максимуму')
extraAx.scatter(array_x[low], array_y[low], \
                marker='o', label='Точки локального мінімуму')
# Так як функція має всього одну точку перетину
# з осями - виведення її без додаткових операцій
extraAx.scatter(0, 0, marker='o', color='black', \
                label='Єдина точка перетину з Ox та Oy')

extraAx.legend(loc='upper right')
plt.show()
