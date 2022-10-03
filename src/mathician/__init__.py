def square(num1):
    return num1 * num1


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


import random
import math


def squareroot(num1):
    return math.sqrt(num1)


def ntroot(num1, num2):
    return num1 ** (1 / num2)


def stringlettercount(String: str):
    stringletters = len(String)
    return stringletters


def fahrenheit_to_celsius(num1):
    answer = num1 - 32 * 0.5556
    return answer


def celsius_to_fahrenheit(num1):
    answer = num1 * 1.8 + 32
    return answer


def randomnumber(num1, num2):
    number = random.randint(num1, num2)
    return number


def ceil(num1):
    ceila = math.ceil(num1)
    return ceila


def floor(num1):
    floora = math.floor(num1)
    return floora


def log(num1, num2):
    loga = math.log(num1, num2)
    return loga


def factorial(num1):
    factoriala = math.factorial(num1)
    return factoriala


def comb(num1, num2):
    comba = math.comb(num1, num2)
    return comba


def pi():
    return math.pi


def pow(num1, num2):
    powa = math.pow(num1, num2)
    return powa


def cos(num1):
    cosa = math.cos(num1)
    return cosa


def remainder(num1, num2):
    remaindera = math.remainder(num1, num2)
    return remaindera


def radians(num1):
    radiana = math.radians(num1)
    return radiana

def integrate(func, a, b, precision):
    total = 0
    dx = (b-a) / precision

    for n in range(0, precision):
        s = a + n*dx
        total += func(s) + func(s + dx)

    return (dx/2) * total