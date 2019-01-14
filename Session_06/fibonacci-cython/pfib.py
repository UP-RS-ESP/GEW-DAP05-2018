import numpy as np

def fibf(n):
    a = 0.0
    b = 1.0
    for i in range(n):
        a, b = a+b, a

    return a

def fibr(n):
    if n == 0 or n == 1:
        a = n
    else:
        a = fibr(n-1)+fibr(n-2)

    return a
