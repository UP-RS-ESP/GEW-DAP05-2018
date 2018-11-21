import numpy as np
from scipy.stats import linregress
from matplotlib import pyplot as pl

def circles_monte_bad(n = 20, m = 1e7):
    m = int(m)
    def counts(r):
        rmax = x.max()
        rx = rmax * (2 * np.random.random(m) - 1)
        ry = rmax * (2 * np.random.random(m) - 1)
        return np.sum(np.sqrt(rx*rx+ry*ry) <= r)

    x = np.logspace(0, 3, n)
    y = np.array([counts(xi) for xi in x])

    return (x, y)

def circles_monte(n = 20, m = 1e7, rmin = 1, rmax = 1000):
    m, n = int(m), int(n)
    x = np.logspace(np.log10(rmin), np.log10(rmax), n)
    rx = x.max() * (2 * np.random.random(m) - 1)
    ry = x.max() * (2 * np.random.random(m) - 1)
    rr = np.sqrt(rx*rx + ry*ry)
    y = np.array([np.sum(rr <= r) for r in x])

    return (x, y)

def show(title, func, **kwargs):
    x, y = func(**kwargs)
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
    pl.loglog(x, p*x**d, 'r-', lw = 1, label = 'fit: y~x^d, d = %.2f' % d)
    pl.xlabel('Size')
    pl.ylabel('Mass')
    pl.grid()
    pl.legend(loc = 'upper left')
    pl.show()

def main():
    show('Monte Carlo circles', circles_monte, rmin = 1, rmax = 1000, m = 1e7)
    #show('Monte Carlo circles (bad)', circles_monte_bad)

if __name__ == '__main__':
    main()
