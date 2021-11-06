from math import pi, pow, sin, cos


def f(_x: float) -> float:
    return pow(sin(_x), 2) + 1


def df(_x: float) -> float:
    return sin(2 * x)


def ddf(_x: float) -> float:
    return 2 * cos(2 * x)


def dLagrange(_x: float, _x0: float, _xn: float, _n: int) -> float:
    _h = (_xn - _x0) / _n
    result = 0
    for i in range(n):
        _tmp = 0
        _pi = 1
        xi = x0 + i * h
        for j in range(n):
            _pij = 1
            if i != j:
                for k in range(n):
                    xk = x0 + k * h
                    if (k != i) and (k != j):
                        _pij *= (x - xk)
                _tmp += _pij
        for z in range(n):
            xz = x0 + z * h
            if z != i:
                _pi *= (xi - xz)
        yi = f(xi)
        result += yi * _tmp / _pi
    return result


def ddLagrange(_x: float, _x0: float, _xn: float, _n: int) -> float:
    _h = (_xn - _x0) / _n
    result = 0
    for i in range(n):
        _sj = 0
        _pi = 1
        xi = x0 + i * h
        for j in range(n):
            if i != j:
                _sk = 0
                for k in range(n):
                    _pijk = 1
                    if k != j and k != i:
                        for z in range(n):
                            xz = x0 + z * h
                            if z != i and z != j and z != k:
                                _pijk *= x - xz
                        _sk += _pijk
                _sj += _sk
        for z in range(n):
            xz = x0 + z * h
            if z != i:
                _pi *= xi - xz
        yi = f(xi)
        result += yi * _sj / _pi
    return result


if __name__ == '__main__':
    n = int(input("Введите порядок интерполяции: "))
    print("Значения производных полинома на новой сетке, погрешности:")
    print(
        "i" + " " * 3 + "x" + "\t" * 3 + "L'(Xi)" + "\t" * 3 + "L''(Xi)" +
        "\t" * 3 + "f'(Xi)" + "\t" * 2 + "f''(Xi)" + "\t" * 2 + "R'" +
        "\t" * 3 + "R''")
    x0 = 0
    # https://portal.tpu.ru/SHARED/l/LASUKOV/vm/Tab1/g2.pdf
    # formula lagrange
    xn = pi / 2
    h = (xn - x0) / n
    for g in range(21):
        x = g * pi / 40
        dy = df(x)
        ddy = ddf(x)
        dL = dLagrange(x, x0, xn, n)
        dLL = ddLagrange(x, x0, xn, n)
        print(f"{g}" + " " * 3 + f"{round(x, 6):.6f}" + "\t" * 1 +
              f"{round(dL, 6):.6f}" + "\t" * 2 +
              f"{round(dLL, 6):.6f}" + "\t" * 2 + f"{round(dy, 6):.6f}" + "\t" +
              f"{round(ddy, 6):.6f}" + "\t" + f"{round(abs(dL - dy), 6):.6f}" +
              "\t" + f"{round(abs(dLL - ddy), 6):.6f}")
