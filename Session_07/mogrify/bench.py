import sys
import numpy as np
from timeit import timeit
from matplotlib import pyplot as pl

number = 1000
m = 40

tc = np.zeros(m)
ty = np.zeros(m)
tg = np.zeros(m)
tp = np.zeros(m)
l = np.logspace(1, 4, m).astype('int')

for i in range(m):
    print(i)
    tc[i] = timeit('mogc(np.zeros(%i))' % l[i],
            setup = 'import numpy as np; from mog import mogc', number = number) / number
    ty[i] = timeit('mogy(np.zeros(%i))' % l[i],
            setup = 'import numpy as np; from mog import mogy', number = number) / number
    tg[i] = timeit('moggy(np.zeros(%i))' % l[i],
            setup = 'import numpy as np; from mog import moggy', number = number) / number
    tp[i] = timeit('mogp(np.zeros(%i))' % l[i],
            setup = 'import numpy as np; from pmog import mogp', number = number) / number

pl.figure(1, (10.24, 7.68))
pl.title('Mogrify benchmark')
pl.plot(l, tp, label = 'Python')
pl.plot(l, tg, label = 'moggy Cython')
pl.plot(l, ty, label = 'Cython')
pl.plot(l, tc, label = 'C')
pl.xlabel('Length of numpy array')
pl.ylabel('Time [s]')
#ax = pl.gca()
#ax.set_xscale('log')
#ax.set_yscale('log')
pl.legend(loc = 'upper left')
#pl.show()
pl.savefig('%s.pdf' % sys.argv[0][:-3])
