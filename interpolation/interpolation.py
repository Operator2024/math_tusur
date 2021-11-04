from math import pi, pow, sin, factorial


def f(_x: float) -> float:
    return pow(sin(_x), 2) + 1


def fLagrange(_x: float, _x0: float, _xn: float, _n: int) -> float:
    _h = (_xn - _x0) / _n
    result = 0
    for z in range(_n):
        l = 1
        xi = _x0 + z * _h
        for j in range(_n):
            xj = _x0 + j * _h
            if z != j:
                l *= (_x - xj) / (xi - xj)
        yi = f(xi)
        result += yi * l
    return result


def r(_x: float, _x0: float, _h: float, _a: float, _b: float, _n: int) -> float:
    result = 1
    q = (_x - _x0) / _h
    xi = (_a + _b) / 2
    for i in range(_n + 1):
        result *= q - i
    result = f(xi) * result * _h ** _n + 1 / factorial(_n + 1)
    return result


if __name__ == '__main__':
    n = int(input("Введите порядок интерполяции: "))
    print("Значение полиномов на новой сетке:")
    print("i" + " " * 3 + "Xi" + "\t" * 3 + "L(Xi)" + "\t" * 3 + "f(Xi)" +
          "\t" * 2 + "Погрешность")
    x0 = 0
    xn = pi / 2
    h = (xn - x0) / n
    for i in range(21):
        x = i * pi / 40
        y = f(x)
        print(f"{i}" + " " * 3 + f"{round(x, 6):.6f}" + "\t" * 1 +
              f"{round(fLagrange(x, x0, xn, n), 6):.6f}" + "\t" * 2 +
              f"{round(y, 6):.6f}" + "\t" +
              f"{round(r(x, x0, h, x0, xn, n), 6):.6f}")
