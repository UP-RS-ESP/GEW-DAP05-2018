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
    pl.title('Coastline of Britain')
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
    #pl.show()

def coastline(basename = 'lines', n = 1000):
    import shapefile
    
    sf = shapefile.Reader(basename)
    s = sf.shape(0)
    p = np.array(s.points)
    xr = p[:, 0]
    yr = p[:, 1]
    for i in range(1, n):
        s = sf.shape(i)
        p = np.array(s.points)
        xr = np.append(xr, p[:, 0])
        yr = np.append(yr, p[:, 1])

    b = (xr < 1.765) * (yr > 49.958)
    xr = xr[b]
    yr = yr[b]

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
        pl.pcolormesh(xb, yb, z, alpha = 0.8)
        ax = pl.gca()
        ax.set_aspect('equal')
        pl.tight_layout()
        pl.show()
        pl.close('all')
        y[i] = z.sum()

    return (x, y)

def main():
    xr, yr = coastline()
    x, y = boxcount(xr, yr)
    regression(x, y)

if __name__ == '__main__':
    main()
