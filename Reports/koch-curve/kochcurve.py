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

pl.rc('text', usetex = True)
pl.rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
pl.figure(1, (8, 3))

for i in range(5):
    xr = [0.,]
    yr = [0.,]
    koch(xr[0], yr[0], 1, 0, i)
    xr = np.array(xr, dtype = 'float')
    yr = np.array(yr, dtype = 'float')
    pl.plot(xr, yr, label = 'order %i' % i)

pl.legend(loc = 'upper left')
ax = pl.gca()
ax.set_aspect('equal')
pl.tight_layout()
pl.savefig('%s.pdf' % sys.argv[0][:-3])
