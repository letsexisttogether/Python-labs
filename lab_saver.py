import numpy as np
import matplotlib.pyplot as plt
import os


def cut(numObj, digits=0):
    return f"{numObj:.{digits}f}"


# figure is a window to replace graphics on
# axes is a graphic which is placed there
figure, axes = plt.subplots()
axes.set_title("Графік варіанту №3")
axes.set_xlabel("Вісь X")
axes.set_ylabel("Вісь Y")

while True:
    os.system("cls")
    x_start = float(cut(float(input("Enter x_start: ")) * np.pi, 4))
    x_end = float(cut(float(input("Enter x_end: ")) * np.pi, 4))
    step = float(cut(float(input("Enter the step: ")) * np.pi, 4))
    array_x = np.linspace(x_start, x_end, int((x_end - x_start) / step))
    for i in range(0, len(array_x) - 1):
        if np.cos(array_x[i]) == 0:
            array_x[i] = np.nan
    # array_x[(np.cos(array_x) == 0)] = np.nan
    axes.plot(array_x, array_x / np.cos(array_x), color="blue", linestyle='--')
    for element in array_x:
        print("{:.4f} {:.4f}".format(element, np.cos(element)))
    plt.show()
