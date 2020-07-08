import numpy as np


def bubble_max_row(a, col):
    max_element = a[col][col]
    max_row = col
    for i in range(col + 1, len(a)):
        if abs(a[i][col]) > abs(max_element):
            max_element = a[i][col]
            max_row = i
        if max_row != col:
            a[col], a[max_row] = a[max_row], a[col]


def check_diagonal(array):
    for i in range(len(array)):
        if not array[i][i]:
            return True
    else:
        return False


def solve(a):
    for i in range(len(a) - 1):
        bubble_max_row(a, i)
        for j in range(i + 1, len(a)):
            if a[i][i] == 0:
                return "Нет решений"
            div = a[j][i] / a[i][i]
            a[j][-1] -= div * a[i][-1]
            for k in range(i, len(a)):
                a[j][k] -= div * a[i][k]
    if check_diagonal(a):
        print('Бесконечное числоо решений')
        return

    x = [0 for i in range(len(a))]
    for i in range(len(a) - 1, -1, -1):
        x[i] = (a[i][-1] - sum([a[i][j] * x[j] for j in range(i + 1, len(a))])) / a[i][i]
    return x


def split_matrix(a):
    matrix_of_unknowns = [[0] * len(a) for i in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a)):
            matrix_of_unknowns[i][j] = a[i][j]
    return matrix_of_unknowns


def split_vector(a):
    b = [0 for i in range(len(a))]
    for i in range(len(a)):
        b[i] = a[i][len(a)]
    return b


def solve_residuals(a):
    if check_diagonal(a):
        return
    b = np.array(split_vector(a))
    s = np.array(solve(a))
    m = np.array(split_matrix(a))
    return b - (np.dot(m, s))


def solve_det(a):
    matr = np.array(split_matrix(a))
    return np.linalg.det(matr)


def print_matrix(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print("|" + "%2.4f" % (a[i][j]), end='|')
        print()


def print_solution(a):
    print("Исходная матрица: ")
    print_matrix(a)
    print("Решение системы: ")
    print(solve(a))
    print("Треугольный вид: ")
    print_matrix(a)
    print("Вектор невязок", solve_residuals(a))
    print("det", solve_det(a))


while 1:
    matrix = str(input("Введите тип объявления матрицы: " + "\n" +
                       "A : консоль " + "\n" +
                       "B : файл" + "\n" +
                       "E : выйти из программы" + "\n"))
    if matrix == "A":
        n = int(input("Введите размерностиь матрицы"))
        if n > 0:
            a = [[0] * (n + 1) for i in range(n)]
            for i in range(n):
                for j in range(n + 1):
                    a[i][j] = int(input("Введите a" + str(i) + str(j)))
            print_solution(a)
        else:
            print("Неверная размерность")

    elif matrix == "B":
        path = str(input("Введите путь:" + "\n"))
        with open(path, 'r') as file:
            a = file.readlines()
        a = [[float(n) for n in x.split()] for x in a]
        print_solution(a)

    elif matrix == "E":
        break

    else:
        print("Неверная команда!!!")
