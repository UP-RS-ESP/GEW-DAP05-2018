import numpy as np
from scipy.stats import linregress
from matplotlib import pyplot as pl

def spheres(n = 10):
    x = np.zeros(n)
    y = np.zeros(n)
    for i in range(n):
        x[i] = i + 1.0
        y[i] = np.pi / 6 * x[i]**3

    return (x, y)

def DINpaper(width0 = 1./np.sqrt(3), n = 10):
    a, b, c = width0, np.sqrt(2)*width0, 1
    x = np.zeros(n)
    y = np.zeros(n)
    for i in range(n):
        x[i] = np.sqrt(a*a+b*b)
        y[i] = c
        a, b, c = b, b*np.sqrt(2), c*2

    return (x, y)

def DINpaper3D(width0 = 1./np.sqrt(3), n = 10):
    a, b, c = width0, np.sqrt(2)*width0, 1
    x = np.zeros(n)
    y = np.zeros(n)
    for i in range(n):
        x[i] = np.sqrt(2*a*a+b*b)
        y[i] = c
        a, b, c = b, b*np.sqrt(2), c*np.sqrt(8)

    return (x, y)

def DINpaperS():
    x = np.array((2.2, 3, 4, 5.5, 7.1, 10))
    y = np.append((1,), np.cumprod(2*np.ones(len(x)-1)))
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

def main(title):
    if title == '3D Spheres':
        show(title, spheres)

    if title == '2D paper':
        show(title, DINpaper)
        #show(title, DINpaper, n=100)

    if title == '3D paper':
        show(title, DINpaper3D)

    if title == 'Crumpled paper balls':
        show(title, DINpaperS)

if __name__ == '__main__':
    main('3D Spheres')
    main('2D paper')
    main('3D paper')
    main('Crumpled paper balls')
