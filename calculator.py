# https://github.com/Shaunish-Pradhan/lab11-SP-AV
# Partner 1: Shaunish Pradhan
# Partner 2: Alona Virichenko
import math


def square_root(a):
    if a < 0:
        raise ValueError("Cannot take the square root of a negative number")
    return math.sqrt(a)


def hypotenuse(a, b):
    return math.hypot(a, b)


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if a == 0:
        raise ZeroDivisionError("a cannot be 0")
    return b / a


def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid base or argument for logarithm")
    return math.log(b, a)


def exp(a, b):
    return a ** b