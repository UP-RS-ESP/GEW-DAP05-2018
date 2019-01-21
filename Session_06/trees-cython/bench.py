import sys
import numpy as np
from timeit import timeit
from matplotlib import pyplot as pl

number = 1000
m = 10

tyr = np.zeros(m)
tym = np.zeros(m)
tpr = np.zeros(m)
tpm = np.zeros(m)

for i in range(m):
    print(i)
    tyr[i] = timeit('SymBinTreeNumpy(0, 0, 1, 0, %i)' % i,
             setup = 'from ytrees import SymBinTreeNumpy', number = number) / number
    tpr[i] = timeit('SymBinTreeNumpy(0, 0, 1, 0, %i)' % i,
             setup = 'from ptrees import SymBinTreeNumpy', number = number) / number
    tym[i] = timeit('SymBinTreeMath(0, 0, 1, 0, %i)' % i,
             setup = 'from ytrees import SymBinTreeMath', number = number) / number
    tpm[i] = timeit('SymBinTreeMath(0, 0, 1, 0, %i)' % i,
             setup = 'from ptrees import SymBinTreeMath', number = number) / number

pl.figure(1, (10.24, 7.68))
pl.title('Symmetric binary tree benchmark')
pl.semilogy(tpr, label = 'Python recursion using Numpy')
pl.semilogy(tyr, label = 'Cython recursion using Numpy')
pl.semilogy(tpm, label = 'Python recursion using Math')
pl.semilogy(tym, label = 'Cython recursion using Math')
pl.xlabel('Order')
pl.ylabel('Time [s]')
pl.legend(loc = 'upper left')
#pl.show()
pl.savefig('%s.pdf' % sys.argv[0][:-3])
