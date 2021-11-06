import time
from math import cos, sin
from typing import *


def myFunc(_x: float) -> float:
    return 10 * cos(_x) - 0.1 * _x ** 2


def myDFunc(_x: float) -> float:
    return -10 * sin(_x) - 0.2 * _x


def distrRoots(_a: Text, _b: Text, n: int) -> Tuple:
    h = (float(_b) - float(_a)) / n
    x = 0
    fx = myFunc(float(_a))
    for i in range(n):
        x = float(_a) + i * h
        fx_next = myFunc(x)
        if fx * fx_next < 0: break
        fx = fx_next
    _a = x - h
    _b = x
    return round(_a, 3), round(_b, 3)


def tangMethod(_a, _b, e1, e2):
    start = time.time_ns()
    x = (_a + _b) / 2
    n = 0
    fx = myFunc(x)
    xn = x / 4
    xn1 = x / 2
    xn2 = x
    while abs(fx) > e2 and abs(xn - xn1) > e1:
        x = x - fx / myDFunc(x)
        xn, xn1 = xn1, xn2
        xn2 = x
        n += 1
        fx = myFunc(x)
    end = time.time_ns() - start
    print(f"Результат, полученный методом Ньютона, x: {x}; количество итераций:"
          f" {n}")
    print(f"f(x): {round(fx, 9)}, \nКоличество вычислений f(x): {n}")
    print(f"Сходимость: {round(abs((xn2 - xn) / pow(xn - xn1, n)), 5)}")
    print(f"Время вычислений: {end}")


if __name__ == '__main__':
    with open("input.txt", "r", encoding="utf8") as file:
        input_file = file.read().split(" ")
        a = input_file[0]
        b = input_file[1]
        eps1 = input_file[2]
        eps2 = input_file[3].rstrip("\n")
    print(f"Уравнение f(x)=0; f(x)=10cos(x)-0.1x^2; корень в отрезке [{a};{b}]")
    print(f"Точности аргумента и функции: {eps1}, {eps2}")
    a, b = distrRoots(a, b, 10)
    print(f"Корень есть в отрезке [{a};{b}]")
    tangMethod(a, b, float(eps1), float(eps2))
