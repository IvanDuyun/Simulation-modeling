from math import pi, log, sqrt, exp, cos
import random

count_exp = 0  # количество опытов моделирования

def random_mid_sqr(n=0, x=0.1723546467563):
    y = []
    for i in range(n):
        x *= x
        x *= 100
        x %= 1
        x = str(x)
        x = float(x[:x.find('e')])
        if x >= 1:
            x %= 1
        y.append(x)
    return y

def random_cong(n):
    y = []
    for i in range(n):
        y.append(random.random())
    return y

def random_irrat_num(n, irnum=pi):
    y = []
    for i in range(0, n):
        x = i * irnum
        x %= 1
        x = float(str(x)[:12])
        if x >= 1:
            x %= 1
        y.append(x)
    return y

def uniform_distribution(x, a, b):
    b += 1
    return a + (b - a) * x

def exponential_distribution(x, lmbd):
    return -log(1 - x) / lmbd

def normal_distribution(x1, x2, m, sigma):
    if x1 <= .0:
        return .0
    if x2 <= .0:
        return .0
    return sigma * cos(2 * pi * x1) * sqrt(-2 * log(x2)) + m

def normal_ideal(i, m, sigma):
    return (1 / (sigma * sqrt(2 * pi))) * exp(-(((i - m) ** 2) / (2 * sigma ** 2)))  # Плотность распределния

def exponential_ideal(x, lmbd):
    return lmbd * exp(- lmbd * x)
