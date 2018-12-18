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
    if int(x0) == int(x1) and int(y0) == int(y1):
        return (int(y0), int(x0))

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

    if dx:
        x = np.append(np.arange(x0, x1, wx), [x1,])
    else:
        y = np.append(np.arange(y0, y1, wy), [y1,])
        x = np.full(len(y), x0)

    if dy:
        y = np.append(np.arange(y0, y1, wy), [y1,])
    else:
        x = np.append(np.arange(x0, x1, wx), [x1,])
        y = np.full(len(x), y0)

    return (y.astype('int'), x.astype('int'))

def show_regression(x, y):
    from scipy.stats import linregress

    fit = linregress(np.log10(x), np.log10(y))
    d = fit.slope
    p = 10**fit.intercept
    pl.title('Koch curve')
    pl.loglog(x, y, 'ko--',
            markersize = 9,
            markerfacecolor = 'none',
            markeredgewidth = 2,
            lw = 2,
            label = 'data')
    pl.loglog(x, p*x**d, 'r-', lw = 1, label = 'fit: y~x^d, d = %.3f, diff = %.3e' % (d, d-np.log(4)/np.log(3)))
    pl.xlabel('1 / width')
    pl.ylabel('Counts')
    pl.grid()
    pl.legend(loc = 'upper left')
    pl.show()

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
    xb = np.arange(-0.01, 1.01+w, w)
    yb = np.arange(-0.01, 0.31+w, w)
    z = np.zeros((len(yb), len(xb)), dtype = 'int')
    for k in range(n-1):
        yl, xl = draw_line((xr[k], yr[k]),
                           (xr[k+1], yr[k+1]),
                           xb, yb)
        z[yl, xl] = 1

    #pl.pcolormesh(xb, yb, z, alpha = 0.8)
    #ax = pl.gca()
    #ax.set_aspect('equal')
    #pl.tight_layout()
    #pl.show()
    #pl.close('all')
    y[i] = z.sum()

show_regression(x, y)
