import numpy as np
import mfd
from matplotlib import pyplot as pl

n = 30
xr = np.linspace(0, 2*1.5, int(n*1.5))
yr = np.linspace(0, 2, n)
x, y = np.meshgrid(xr, yr)
z = np.exp(-x*x-y*y)
w = abs(xr[0]-xr[1])
a = mfd.sca(z, w)
b = np.load('data.npy')
pl.pcolormesh(x, y, (a-b)/a)
pl.colorbar()
ax = pl.gca()
ax.set_aspect('equal')
pl.show()
