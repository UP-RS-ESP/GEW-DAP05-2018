import sys
import numpy as np
from matplotlib import pyplot as pl

def regression(x, y):
    from scipy.stats import linregress
    pl.rc('text', usetex = True)
    pl.rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})

    fit = linregress(np.log10(x), np.log10(y))
    d = fit.slope
    p = 10**fit.intercept
    pl.figure(1, (8, 5))
    pl.title('Coastlines')
    pl.loglog(x, y, 'ko--',
            markersize = 9,
            markerfacecolor = 'none',
            markeredgewidth = 2,
            lw = 2,
            label = 'data')
    pl.loglog(x, p*x**d, 'r-', lw = 1, label = 'fit: $y\propto x^d$, d = %.3f' % d)
    pl.xlabel('1 / Box width')
    pl.ylabel('Counts')
    pl.grid()
    pl.legend(loc = 'upper left')
    pl.tight_layout()
    pl.savefig('%s.pdf' % sys.argv[0][:-3])

def coastline(n, basename = 'lines'):
    import shapefile
    
    sf = shapefile.Reader(basename)
    s = sf.shape(0)
    p = np.array(s.points)
    xr = p[:, 0]
    yr = p[:, 1]
    #n = len(sf.records())
    for i in range(1, n):
        s = sf.shape(i)
        p = np.array(s.points)
        xr = np.append(xr, p[:, 0])
        yr = np.append(yr, p[:, 1])

    return (xr, yr)

def boxcount(xr, yr, wr = np.logspace(-2, 0, 5)):
    x = 1 / wr
    y = np.zeros(x.shape)
    for i in range(x.shape[0]):
        w = wr[i]
        xb = np.arange(xr.min()-w, xr.max()+w, w)
        yb = np.arange(yr.min()-w, yr.max()+w, w)
        z = np.zeros((len(yb), len(xb)), dtype = 'int')
        xmin, xmax = xb.min(), xb.max()
        ymin, ymax = yb.min(), yb.max()
        fx = (xb.shape[0] - 1) / float(xb.max() - xb.min())
        fy = (yb.shape[0] - 1) / float(yb.max() - yb.min())
        xi = (fx * (xr - xb.min())).astype('int')
        yi = (fy * (yr - yb.min())).astype('int')
        z[yi, xi] = 1
        y[i] = z.sum()
        #pl.pcolormesh(xb, yb, z, alpha = 0.8)
        #ax = pl.gca()
        #ax.set_aspect('equal')
        #pl.tight_layout()
        #pl.show()
        #pl.close('all')

    return (x, y)

def main():
    from time import time

    m = 10
    #nr = np.logspace(2, 3.7, m).astype('int')
    nr = np.linspace(100, 1000, m).astype('int')
    ta = np.zeros(m)
    tb = np.zeros(m)
    for i in range(m):
        print(i)
        t0 = time()
        xr, yr = coastline(nr[i])
        t1 = time()
        x, y = boxcount(xr, yr)
        t2 = time()
        ta[i] = t1 - t0
        tb[i] = t2 - t1
    #regression(x, y)
    pl.figure(1, (10.24, 7.68))
    pl.plot(nr, ta, label = 'data')
    pl.plot(nr, tb, label = 'count')
    pl.xlabel('Number of coastline shapes')
    pl.ylabel('Time [s]')
    pl.legend(loc = 'upper left')
    #pl.savefig('%s.png' % sys.argv[0][:-3])
    pl.show()

if __name__ == '__main__':
    main()
