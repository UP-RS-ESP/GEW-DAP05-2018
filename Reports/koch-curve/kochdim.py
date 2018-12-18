import sys
import numpy as np
from matplotlib import pyplot as pl

def show_regression(x, y):
    from scipy.stats import linregress
    pl.rc('text', usetex = True)
    pl.rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})

    fit = linregress(np.log10(x), np.log10(y))
    d = fit.slope
    p = 10**fit.intercept
    pl.figure(1, (8, 5))
    pl.title('Koch curve')
    pl.loglog(x, y, 'ko--',
            markersize = 9,
            markerfacecolor = 'none',
            markeredgewidth = 2,
            lw = 2,
            label = 'data')
    pl.loglog(x, p*x**d, 'r-', lw = 1, label = 'fit: $y\propto x^d$, d = %.3f, err = %.3e' % (d, d-np.log(4)/np.log(3)))
    pl.xlabel('1 / Box width')
    pl.ylabel('Counts')
    pl.grid()
    pl.legend(loc = 'upper left')
    pl.tight_layout()
    pl.savefig('%s.pdf' % sys.argv[0][:-3])
    #pl.show()

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

xr = [0.,]
yr = [0.,]
koch(xr[0], yr[0], 1, 0, 8)
xr = np.array(xr, dtype = 'float')
yr = np.array(yr, dtype = 'float')
n = len(xr)

wr = np.logspace(-3, -1, 10)
x = 1 / wr
y = np.zeros(x.shape)
for i in range(x.shape[0]):
    w = wr[i]
    xb = np.arange(-0.02, 1.02+w, w)
    yb = np.arange(-0.02, 0.31+w, w)
    z = np.zeros((len(yb), len(xb)), dtype = 'int')
    xmin, xmax = xb.min(), xb.max()
    ymin, ymax = yb.min(), yb.max()
    fx = (xb.shape[0] - 1) / float(xb.max() - xb.min())
    fy = (yb.shape[0] - 1) / float(yb.max() - yb.min())
    xi = (fx * (xr - xb.min())).astype('int')
    yi = (fy * (yr - yb.min())).astype('int')
    z[yi, xi] = 1

    #pl.pcolormesh(xb, yb, z, alpha = 0.8)
    #ax = pl.gca()
    #ax.set_aspect('equal')
    #pl.tight_layout()
    #pl.show()
    #pl.close('all')
    y[i] = z.sum()

show_regression(x, y)
