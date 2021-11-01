import re

from numpy import *


def readMatrix() -> ndarray:
    n: int = 0
    with open("matrix.txt", "r", encoding="utf8") as file:
        for i, v in enumerate(file.read().split("\n")):
            if i == 0:
                n = int(v)
                matrix = arange((n ** 2) * 2, dtype=float).reshape(n, n * 2)
            else:
                if v != "":
                    for idx, val in enumerate(
                            re.sub("\s{2,}", " ", v).split(" ")
                    ):
                        matrix[i - 1][idx] = val
            if i > 0 and v != "":
                matrix[i - 1][n + (i - 1)] = 1
                for j in range(n, 2 * n):
                    if matrix[i - 1][j] != 1:
                        matrix[i - 1][j] = 0
    return matrix


def showMatrix(_matrix: ndarray, _mode=1):
    if _mode == 1:
        print("Исходная матрица с единичной матрицей:")
        print(_matrix, "\nЕдиничная матрица:\n", eye(_matrix.shape[0]))
        invGauss(_matrix)
    else:
        print(_matrix)


def invGauss(_matrix):
    print("Промежуточные результаты:")
    n = _matrix.shape[0]
    for i in range(n):
        a = _matrix[i][i]
        print(f"Итерация {i + 1}:")
        for j in range(2 * n):
            _matrix[i][j] = _matrix[i][j] / a
        for k in range(n):
            b = _matrix[k][i]
            for z in range(2 * n):
                if k != i:
                    _matrix[k][z] = -_matrix[i][z] * b + _matrix[k][z]
        showMatrix(_matrix, _mode=2)
    print("Обратная матрица по методу Гаусса:")

    for i in range(n):
        output = ""
        for j in range(n):
            output += f"{round(_matrix[i][n + j], 8)}\t"
        print(output + "\n")


if __name__ == '__main__':
    showMatrix(readMatrix())
