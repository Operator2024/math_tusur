from math import exp, cos

from numpy import polynomial, ndarray


def f(_x: float) -> float:
    return exp(-_x ** 2) * cos(_x)


def fGauss(a: float, b: float, n: int) -> float:
    result = 0
    for i in range(n):
        x = ((b + a) + (b - a) * t[i]) / 2
        result += + A[i] * f(x)
    return (b - a) / 2 * result


def fSimpson(a: float, b: float, z: int) -> float:
    # formula Cotes
    h = (b - a) / z
    _n = int(z / 2)
    result = 0
    for i in range(_n):
        x = h * (2 * i) + a
        result += 2 * f(x)
    for j in range(_n):
        x = h * (2 * j + 1) + a
        result += 4 * f(x)
    result += f(a) + f(b)
    return result * h / 3


if __name__ == '__main__':
    # iteration counter C
    C = 0
    n = 6
    # t - Legendre points, A - Legendre weights
    t: ndarray = polynomial.legendre.leggauss(n)[0]
    A: ndarray = polynomial.legendre.leggauss(n)[1]
    print(f"Функция: f(x)=exp(-x^2)*cos(x), a={-float('inf')},b={float('inf')}")
    print(f"Результат полученный методом Гаусса:"
          f" {round(fGauss(-1.97, 1.97, n), n)}")
    # Simpson variables
    eps = 0.001
    a, b = -10, 10
    n = 2
    R1, R2 = 0, fSimpson(a, b, n)
    while (abs(R1 - R2) / R2) > eps:
        n += 2
        R1, R2 = R2, fSimpson(a, b, n)
        C += 1
    print(f"Результат полученный методом Симпсона:"
          f" {round(R2, 6)}, кол-во интервалов: {C + 1}")
