import sys
import numpy as np
from matplotlib import pyplot as pl

def draw_line(p0, p1, xb, yb):
    assert xb.ndim == 1, 'xb not flat'
    assert yb.ndim == 1, 'yb not flat'
    xmin, xmax = xb.min(), xb.max()
    ymin, ymax = yb.min(), yb.max()
    fx = (xb.shape[0] - 1) / float(xmax - xmin)
    fy = (yb.shape[0] - 1) / float(ymax - ymin)
    x0, y0 = fx * (p0[0] - xmin), fy * (p0[1] - ymin)
    x1, y1 = fx * (p1[0] - xmin), fy * (p1[1] - ymin)
    dx = x1 - x0
    dy = y1 - y0
    sx = np.sign(dx)
    sy = np.sign(dy)
    m = abs(dy / dx)
    if m <= 1:
        wx = sx
        wy = m * sy
    else:
        wx = sx / m
        wy = sy
    
    x = np.append(np.arange(x0, x1, wx), [x1,])
    y = np.append(np.arange(y0, y1, wy), [y1,])

    return (y.astype('int'), x.astype('int'))

def show_regression(title, x, y):
    from scipy.stats import linregress

    fit = linregress(np.log10(x), np.log10(y))
    d = fit.slope
    p = 10**fit.intercept
    pl.title(title)
    pl.loglog(x, y, 'ko--',
            markersize = 9,
            markerfacecolor = 'none',
            markeredgewidth = 2,
            lw = 2,
            label = 'data')
    pl.loglog(x, p*x**d, 'r-', lw = 1, label = 'fit: y~x^d, d = %.3f' % d)
    pl.xlabel('1 / width')
    pl.ylabel('Counts')
    pl.grid()
    pl.legend(loc = 'upper left')
    pl.show()

pts = np.random.random((3, 2))
wr = np.logspace(-4, 0, 15)
x = 1 / wr
y = np.zeros(x.shape)
for i in range(x.shape[0]):
    w = wr[i]
    xb = np.arange(0, 1+w, w)
    yb = np.arange(0, 1+w, w)
    z = np.zeros((len(yb), len(xb)), dtype = 'int')
    for j in range(pts.shape[0]):
        for k in range(j):
            yl, xl = draw_line(pts[j], pts[k], xb, yb)
            z[yl, xl] = 1

    #pl.pcolormesh(xb, yb, z, alpha = 0.8)
    #ax = pl.gca()
    #ax.set_aspect('equal')
    #pl.show()
    #pl.close('all')
    y[i] = z.sum()

show_regression('triangle', x, y)
