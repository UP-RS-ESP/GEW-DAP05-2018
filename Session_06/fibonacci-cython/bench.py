import sys
import numpy as np
from timeit import timeit
from matplotlib import pyplot as pl

number = 10000
m = 15

tyr = np.zeros(m)
tyf = np.zeros(m)
tpr = np.zeros(m)
tpf = np.zeros(m)

for i in range(m):
    tyr[i] = timeit('fibyr(%i)' % i,
             setup = 'from fib import fibyr', number = number) / number
    tyf[i] = timeit('fibyf(%i)' % i,
             setup = 'from fib import fibyf', number = number) / number
    tpr[i] = timeit('fibr(%i)' % i,
             setup = 'from pfib import fibr', number = number) / number
    tpf[i] = timeit('fibf(%i)' % i,
             setup = 'from pfib import fibf', number = number) / number

pl.figure(1, (10.24, 7.68))
pl.title('Fibonacci benchmark')
pl.semilogy(tpr, label = 'Python recursion')
pl.semilogy(tpf, label = 'Python for loop')
pl.semilogy(tyr, label = 'Cython recursion')
pl.semilogy(tyf, label = 'Cython for loop')
pl.xlabel('Interation / Fibonacci number')
pl.ylabel('Time [s]')
pl.legend(loc = 'upper left')
pl.show()
