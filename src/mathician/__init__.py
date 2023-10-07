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

from math import *
def square(num):
    """
    Square a number.
    """
    return pow(num,2)

def solutions(a,b,c):
    """
    Find the number of real solutions that are in a quadratic equation with values of ax^2 + bx + c with a,b,c values being inputted respectively.
    
    Note that a value of 0 means 0 real solutions while 1 means 1 real solution and 2 means 2 real solutions.
    """
    d_value = pow(b,2) - 4 * a * c
    if d_value < 0:
        return 0
    elif d_value == 0:
        return 1
    else:
        return 2

def slope(c1,c2):
    """
    Input 2 coordinates as tuples or 2 lists and get the slope of them!
    """
    try:
        return ((c1[1] - c2[1]))/((c1[0] - c2[0]))
    except ZeroDivisionError:
        return 0
def combination(r,n):
    """
    Get a combination of r items fron set of n items.
    """
    return (math.factorial(n)) / math.factorial(r) * math.factorial((n-r))
