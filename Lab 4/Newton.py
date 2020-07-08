import numpy as np
import matplotlib.pyplot as plt
from math import pi

fsin = lambda x: np.sin(x)
fatan = lambda x: np.arctan(x)
fbig = lambda x: np.cos(x) * (x ** 2 + np.sin(x) - 1)


def coef(x, y):
    x.astype(float)
    y.astype(float)
    n = len(x)
    a = []
    for i in range(n):
        a.append(y[i])
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            a[i] = float(a[i] - a[i - 1]) / float(x[i] - x[i - j])
    return np.array(a)


def newton_method(a, x, r):
    x.astype(float)
    n = len(a) - 1
    temp = a[n]
    for i in range(n - 1, -1, -1):
        temp = temp * (r - x[i]) + a[i]
    return temp


def plot_graphic(x, a, y, func):
    xnew = np.linspace(np.min(x), np.max(x), 200)
    ynew = [newton_method(a, x, i) for i in xnew]
    plt.plot(x, y, 'o', xnew, ynew, label="dots")
    ylist = [func(xData) for xData in xnew]
    plt.plot(xnew, ylist, label="true func")
    plt.grid(True)
    plt.legend()
    plt.show()


def enter_args(func):
    dotsx = np.asarray(input("Введите точки").split()).astype(int)
    dotsy = np.array([func(x) for x in dotsx])
    a = coef(dotsx, dotsy)
    plot_graphic(dotsx, a, dotsy, func)


# while 1:
#     choseFunc = str(input("Выберите функцию: \n"
#                           "1) sin(x)\n"
#                           "2) arctan(x)\n"
#                           "3) (x^2 + sin(x) - 1) * cos(x)\n"
#                           "q) выход\n"))
#     if choseFunc == str(1):
#         try:
#             enter_args(fsin)
#         except Exception:
#             print("Шото пошло не так")
#     elif choseFunc == str(2):
#         try:
#             enter_args(fatan)
#         except Exception:
#             print("Шото пошло не так")
#     elif choseFunc == str(3):
#         try:
#             enter_args(fbig)
#         except Exception:
#             print("Шото пошло не так")
#     elif choseFunc == "q":
#         break
#     else:
#         print("Ошибка ввода, попробуйте еще разок")
