import sys
import numpy as np
import shapefile
from matplotlib import pyplot as pl

basefname = 'lines'
sf = shapefile.Reader(basefname)

#n = len(sf.records())
#print(n)

s = sf.shape(0)
p = np.array(s.points)
x = p[:, 0]
y = p[:, 1]

for i in range(1, 1000):
    s = sf.shape(i)
    p = np.array(s.points)
    x = np.append(x, p[:, 0])
    y = np.append(y, p[:, 1])

b = (x < 1.765) * (y > 49.958)
x = x[b]
y = y[b]
pl.plot(x, y, 'k,')
a = pl.gca()
a.set_aspect('equal')
pl.show()
