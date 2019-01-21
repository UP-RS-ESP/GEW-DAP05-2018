import numpy as np
from math import cos, sin

def SymBinTreeNumpy(x, y, rho, phi, order):
    xn, yn = x + rho * np.cos(phi), y + rho * np.sin(phi)
    if order:
        SymBinTreeNumpy(xn, yn, 0.62 * rho, phi + np.pi / 3, order - 1)
        SymBinTreeNumpy(xn, yn, 0.62 * rho, phi - np.pi / 3, order - 1)

def SymBinTreeMath(x, y, rho, phi, order):
    xn, yn = x + rho * cos(phi), y + rho * sin(phi)
    if order:
        SymBinTreeMath(xn, yn, 0.62 * rho, phi + np.pi / 3, order - 1)
        SymBinTreeMath(xn, yn, 0.62 * rho, phi - np.pi / 3, order - 1)

