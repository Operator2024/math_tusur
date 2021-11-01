import re

from numpy import *


def readMatrix() -> ndarray:
    n: int = 0
    with open("matrix.txt", "r", encoding="utf8") as file:
        for i, v in enumerate(file.read().split("\n")):
            if i == 0:
                n = int(v)
                matrix = arange(n ** 2, dtype="f8").reshape(n, n)
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


def invGauss(_matrix: ndarray) -> float:
    n = _matrix.shape[0]
    d = 1
    print("Промежуточные результаты:")
    for i in range(n - 1, 0, -1):
        print(f"Итерация {n - i}")
        for j in range(0, i, 1):
            a = _matrix[j][i]
            b = _matrix[j + 1][i]
            for k in range(n):
                if abs(-_matrix[j][k] * b + _matrix[j + 1][k] * a) == 0:
                    _matrix[j][k] = 0.0
                else:
                    _matrix[j][k] = -_matrix[j][k] * b + _matrix[j + 1][k] * a
            d = d / (-b)
        showMatrix(_matrix, _mode=2)
    print(f"Определитель: {round(d, 14)}")
    for i in range(n):
        d = d * _matrix[i][i]
    return d


if __name__ == '__main__':
    print(f"По методу Гаусса |A|: {round(showMatrix(readMatrix()), 3)}")
