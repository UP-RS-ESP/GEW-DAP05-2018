import sys
import numpy as np
from timeit import timeit
from matplotlib import pyplot as pl

number = 1000
m = 20

tcr = np.zeros(m)
tcf = np.zeros(m)
tyr = np.zeros(m)
tyf = np.zeros(m)
tpr = np.zeros(m)
tpf = np.zeros(m)

for i in range(m):
    print(i)
    tcr[i] = timeit('fibcr(%i)' % i,
             setup = 'from fib import fibcr', number = number) / number
    tcf[i] = timeit('fibcf(%i)' % i,
             setup = 'from fib import fibcf', number = number) / number
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
pl.semilogy(tcr, label = 'C recursion')
pl.semilogy(tcf, label = 'C for loop')
pl.xlabel('Interation / Fibonacci number')
pl.ylabel('Time [s]')
pl.xticks(range(m))
pl.legend(loc = 'upper left')
#pl.show()
pl.savefig('%s.pdf' % sys.argv[0][:-3])
