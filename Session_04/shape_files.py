import numpy as np
import shapefile
from matplotlib import pyplot as pl

basefname = sys.argv[1]
sf = shapefile.Reader(basefname)

#n = len(sf.records())
#print(n)

for i in range(1000):
    s = sf.shape(i)
    p = np.array(s.points)
    pl.plot(p[:, 0], p[:, 1])

pl.show()
