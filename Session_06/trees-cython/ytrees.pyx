import numpy as np
from math import cos, sin

def SymBinTreeNumpy(double x, double y,
                    double rho, double phi,
                    int order):
    cdef double xn, yn
    if order:
        xn = x + rho * np.cos(phi)
        yn = y + rho * np.sin(phi)
        SymBinTreeNumpy(xn, yn, 0.62 * rho, phi + np.pi / 3, order - 1)
        SymBinTreeNumpy(xn, yn, 0.62 * rho, phi - np.pi / 3, order - 1)

def SymBinTreeMath(double x, double y,
                   double rho, double phi,
                   int order):
    cdef double xn, yn
    if order:
        xn = x + rho * cos(phi)
        yn = y + rho * sin(phi)
        SymBinTreeMath(xn, yn, 0.62 * rho, phi + np.pi / 3, order - 1)
        SymBinTreeMath(xn, yn, 0.62 * rho, phi - np.pi / 3, order - 1)

