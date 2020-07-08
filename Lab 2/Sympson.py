import math
import numpy as np

class Sympson:
    __sum = 0.0
    __nsegment = 1  # число отрезков разбиения

    def __restart(func, x0, x1, nseg0, reset_calls=True):
        Sympson.__nsegment = nseg0
        Sympson.__sum = 0.5 * (func(x0) + func(x1))
        dx = 1.0 * (x1 - x0) / nseg0
        for i in range(1, nseg0):
            Sympson.__sum += func(x0 + i * dx)
        return Sympson.__sum * dx

    def __doubling_nsegment(func, x0, x1):
        nseg = Sympson.__nsegment
        dx = (x1 - x0) / nseg
        x = x0 + 0.5 * dx
        i = 0
        AddedSum = 0.0
        for i in range(nseg):
            AddedSum += func(x + i * dx)
        Sympson.__sum += AddedSum
        Sympson.__nsegment *= 2
        return Sympson.__sum * 0.5 * dx

    def simpson(func, x0, x1, accuracy=1.0e-10, nsegment0=1):
        if accuracy <= 0:
            return print("Неверная точность")
        old_sum = Sympson.__restart(func, x0, x1, nsegment0)
        new_sum = Sympson.__doubling_nsegment(func, x0, x1)
        ans = (4 * new_sum - old_sum) / 3
        old_ans = 0.0
        err_est = max(1, abs(ans))
        while err_est > abs(accuracy * ans):
            old_ans = ans
            old_sum = new_sum
            new_sum = Sympson.__doubling_nsegment(func, x0, x1)
            ans = (4 * new_sum - old_sum) / 3
            err_est = abs(old_ans - ans)
        return abs(ans), err_est, Sympson.__nsegment


while 1:
    fu = str(input("Введите номер функции интеграл от которой вы хотите вычислить:" + "\n" +
                   "1)y = x" + "\n" +
                   "2)y = x^2" + "\n" +
                   "3)y = 2x+1/(sqrt(x)+1/16))" + "\n" +
                   "4)y = sqrt(x)" + "\n" +
                   "5)y = sin(x)/x" + "\n" +
                   "6)y = 1/x"))
    if fu == str(1):
        x1 = float(input("Введите нижнюю границу"))
        x0 = float(input("Введите верхнюю границу"))
        accuracy = float(input("Введите точность"))
        ans = Sympson.simpson(lambda x: np.sin(x), x0, x1, accuracy)
        print("Ответ: ", ans[0])
        print("Погрешность: ", ans[1])
        print("Количество разбиений: ", ans[2])
    elif fu == str(2):
        x1 = float(input("Введите нижнюю границу"))
        x0 = float(input("Введите верхнюю границу"))
        accuracy = float(input("Введите точность"))
        ans = Sympson.simpson(lambda x: x ** 2, x0, x1, accuracy)
        print("Ответ: ", ans[0])
        print("Погрешность: ", ans[1])
        print("Количество разбиений: ", ans[2])
    elif fu == str(3):
        x1 = float(input("Введите нижнюю границу"))
        x0 = float(input("Введите верхнюю границу"))
        accuracy = float(input("Введите точность"))
        if x1 <= 0 or x0 <= 0:
            print("Невозможно вычислить интеграл, выход за рамки ОДЗ")
        else:
            ans = Sympson.simpson(lambda x: 2 * x + 1 / math.sqrt((x) + 1 / 16), x0, x1, accuracy)
            print("Ответ: ", ans[0])
            print("Погрешность: ", ans[1])
            print("Количество разбиений: ", ans[2])
    elif fu == str(4):
        x1 = float(input("Введите нижнюю границу"))
        x0 = float(input("Введите верхнюю границу"))
        accuracy = float(input("Введите точность"))
        if x1 <= 0 or x0 <= 0:
            print("Невозможно вычислить интеграл, выход за рамки ОДЗ")
        else:
            ans = Sympson.simpson(lambda x: math.sqrt(x), x0, x1, accuracy)
            print("Ответ: ", ans[0])
            print("Погрешность: ", ans[1])
            print("Количество разбиений: ", ans[2])
    elif fu == str(5):
        x1 = float(input("Введите нижнюю границу"))
        x0 = float(input("Введите верхнюю границу"))
        accuracy = float(input("Введите точность"))
        if x1 == 0 or x0 == 0 or (x0 < 0 and x1 > 0) or (x1 < 0 and x0 > 0):
            x0 -= 0.000001
            x1 += 0.000001
            ans = Sympson.simpson(lambda x: math.sin(x) / x, x0, 0.01)
            ans += Sympson.simpson(lambda x: math.sin(x) / x, 0.01, x1)
            print("Ответ: ", ans[0])
            print("Погрешность: ", ans[1])
            print("Количество разбиений:", ans[2])
        else:
            Sympson.simpson(lambda x: math.sin(x) / x, x0, x1, accuracy)
    elif fu == str(6):
        x1 = float(input("Введите нижнюю границу"))
        x0 = float(input("Введите верхнюю границу"))
        accuracy = float(input("Введите точность"))
        if x1 == 0 or x0 == 0 or (x0 < 0 and x1 > 0) or (x1 < 0 and x0 > 0):
            # x0 -= 0.000001
            # x1 += 0.000001
            # ans = Sympson.simpson(lambda x: 1 / x, x0, 0.01, accuracy)
            # ans += Sympson.simpson(lambda x: 1 / x, 0.01, x1, accuracy)
            # print("Ответ: ", ans[0])
            # print("Погрешность: ", ans[1])
            # print("Количество разбиений: ", ans[2])
            print("Невозможно вычислить интеграл? Точка разрыва 2 рода." + "\n")
        else:
            ans = Sympson.simpson(lambda x: 1 / x, x0, x1, accuracy)
            print("Ответ: ", ans[0])
            print("Погрешность: ", ans[1])
            print("Количество разбиений: ", ans[2])
    else:
        print("Неверный номер")