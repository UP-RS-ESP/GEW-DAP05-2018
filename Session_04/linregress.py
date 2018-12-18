import numpy as np
from matplotlib import pyplot as pl
from scipy.stats import linregress

def show_regression(x, y):
    fit = linregress(x, y)
    a = fit.slope
    b = fit.intercept
    pl.plot(x, y, 'ko--',
            markersize = 9,
            markerfacecolor = 'none',
            markeredgewidth = 2,
            lw = 2,
            label = 'data')
    pl.plot(x, a*x+b, 'r-', lw = 1,
            label = 'fit: $y=ax+b$, a=%.3f, b=%.3f' % (a, b))
    pl.grid()
    pl.legend(loc = 'upper left')
    pl.show()

# fill in values from derivation by hand
x = np.array([-1, 0, 1])
y = np.array([-1.1, 1.5, 2.7])
show_regression(x, y)
