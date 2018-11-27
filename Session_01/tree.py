import sys
import numpy as np
from matplotlib import pyplot as pl

def tree(x, y, rho, phi, order):
    xn, yn = x + rho * np.cos(phi), y + rho * np.sin(phi)
    pl.plot([x, xn], [y, yn])
    if order:
        tree(xn, yn, 0.62 * rho, phi + np.pi / 3, order - 1)
        tree(xn, yn, 0.62 * rho, phi - np.pi / 3, order - 1)

tree(0, 0, 1, 0, int(sys.argv[1]))
ax = pl.gca()
ax.set_aspect('equal')
pl.grid()
pl.show()
