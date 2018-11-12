import sys
import numpy as np
from matplotlib import pyplot as pl

def spiral(x, y, rho, phi):
    xn, yn = x + rho * np.cos(phi), y + rho * np.sin(phi)
    pl.plot([x, xn], [y, yn])
    try:
        spiral(xn, yn, 0.7 * rho, phi + np.pi / 4)
    except Exception:
        # ignore the RuntimeError: maximum recursion depth exceeded
        pass

pl.figure()
sys.setrecursionlimit(100)
spiral(0, 0, 1, 0)
pl.show()
