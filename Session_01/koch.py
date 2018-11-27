import sys
import numpy as np
from matplotlib import pyplot as pl

def koch(x0, y0, rho, phi, order):
    global xr, yr

    x1, y1 = x0 + rho * np.cos(phi), y0 + rho * np.sin(phi)
    if order:
        x, y = x0, y0
        for angle in [0, np.pi/3, 5*np.pi/3, 0]:
            x, y = koch(x, y, rho / 3.0, phi + angle, order - 1)
    else:
        xr.append(x1)
        yr.append(y1)

    return (x1, y1)

xr = [1,]
yr = [1,]
koch(xr[0], yr[0], 1, 0, 5)
pl.plot(xr, yr, 'r.-', lw = 0.5)
ax = pl.gca()
ax.set_aspect('equal')
pl.grid()
pl.show()
