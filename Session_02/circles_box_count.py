import numpy as np
from scipy.stats import linregress
from matplotlib import pyplot as pl

def circles_boxcount(r = 1, n = 10):
    w = np.logspace(np.log10(r*0.001), np.log10(r*0.1), n)
    x = 1./w
    y = np.zeros(n)
    for i in range(n):
        xc, yc = np.meshgrid(np.arange(-r, r+w[i], w[i]),
                             np.arange(-r, r+w[i], w[i]))
        rc = np.sqrt(xc*xc + yc*yc)
        y[i] = np.sum(rc <= r)

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
    pl.loglog(x, p*x**d, 'r-', lw = 1, label = 'fit: y~x^d, d = %.3f' % d)
    pl.xlabel('1 / width')
    pl.ylabel('Counts')
    pl.grid()
    pl.legend(loc = 'upper left')
    pl.show()

def main():
    show('Circles box count', circles_boxcount)

if __name__ == '__main__':
    main()
