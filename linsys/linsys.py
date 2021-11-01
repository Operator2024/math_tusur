import re
from copy import deepcopy

from numpy import *


def readMatrix() -> ndarray:
    n: int = 0
    with open("matrix.txt", "r", encoding="utf8") as file:
        for i, v in enumerate(file.read().split("\n")):
            if i == 0:
                n = int(v)
                matrix = arange((n ** 2) + n, dtype=float).reshape(n, n + 1)
                set_printoptions(precision=8, suppress=True)
            else:
                if v != "":
                    for idx, val in enumerate(
                            re.sub("\s{2,}", " ", v).split(" ")
                    ):
                        matrix[i - 1][idx] = val
    return matrix


def showMatrix(_matrix: ndarray, _mode=1):
    if _mode == 1:
        print(f"Исходная матрица: \n{_matrix}")
        return invGauss(_matrix)
    else:
        print(_matrix)


def invGauss(_matrix: ndarray):
    n = _matrix.shape[0]
    A = deepcopy(_matrix)
    print("Промежуточные результаты прямого хода:")
    for i in range(n - 1, 0, -1):
        for j in range(0, i, 1):
            a = _matrix[j][i]
            b = _matrix[j + 1][i]
            for k in range(n + 1):
                _matrix[j][k] = -_matrix[j][k] * b + _matrix[j + 1][k] * a
        print(f"Итерация {n - i}")
        showMatrix(_matrix, _mode=2)

    X = arange(n, dtype=float).reshape(n, 1)
    for i in range(n):
        X[i] = _matrix[i][n]
        for j in range(i):
            X[i] = X[i] - _matrix[i][j] * X[j]
        if _matrix[i][i] == 0:
            print("Метод Гаусса: матрица вырождена\n")
            return
        X[i] = X[i] / _matrix[i][i]
    print(f"Метод Гаусса: x={[round(X[i][0], 5) for i in range(n)]}")
    norm = 0
    X1 = deepcopy(X)
    for i in range(n):
        X1[i] = 0
        for j in range(n):
            X1[i] = X1[i] + X[j] * A[i][j]
        X1[i] = X1[i] - A[i][n]
        if norm < abs(X1[i]):
            norm = X1[i]
    print(f"Невязка: {round(norm[0], 20)}")
    return


if __name__ == '__main__':
    showMatrix(readMatrix())
