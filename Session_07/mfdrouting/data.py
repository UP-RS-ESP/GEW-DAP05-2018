import numpy as np
from mfdrouting import SCA
#from matplotlib import pyplot as pl

n = 30
xr = np.linspace(0, 2*1.5, int(n*1.5))
yr = np.linspace(0, 2, n)
x, y = np.meshgrid(xr, yr)
z = np.exp(-x*x-y*y)

#pl.pcolormesh(x, y, z)
#pl.colorbar()
#ax = pl.gca()
#ax.set_aspect('equal')
#pl.show()
w = abs(xr[0]-xr[1])
a = SCA(z, w)
np.save('data.npy', a)
