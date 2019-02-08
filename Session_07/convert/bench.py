import sys
import numpy as np
from timeit import timeit
from matplotlib import pyplot as pl

number = 1000
m = 15

ty = np.zeros(m)
tc = np.zeros(m)
tn = np.zeros(m)
tp = np.zeros(m)
l = np.logspace(1, 2.5, m).astype('int')

for i in range(m):
    print(i)
    tc[i] = timeit('vrtc(np.zeros((%i,%i)))' % (l[i], l[i]),
            setup = 'import numpy as np; from vrt import vrtc', number = number) / number
    ty[i] = timeit('vrty(np.zeros((%i, %i)))' % (l[i], l[i]),
            setup = 'import numpy as np; from vrt import vrty', number = number) / number
    tn[i] = timeit('vrty_naive(np.zeros((%i,%i)))' % (l[i], l[i]),
            setup = 'import numpy as np; from vrt import vrty_naive', number = number) / number
    tp[i] = timeit('vrty_naive(np.zeros((%i, %i)))' % (l[i], l[i]),
            setup = 'import numpy as np; from pvrt import vrty_naive', number = number) / number

pl.figure(1, (10.24, 7.68))
pl.title('Convert benchmark')
pl.plot(l*l, tc, label = 'C')
pl.plot(l*l, ty, label = 'Cython')
pl.plot(l*l, tn, label = 'Cython naive')
pl.plot(l*l, tp, label = 'Python')
pl.xlabel('Length of numpy array')
pl.ylabel('Time [s]')
ax = pl.gca()
ax.set_xscale('log')
ax.set_yscale('log')
pl.legend(loc = 'upper left')
#pl.show()
pl.savefig('%s.pdf' % sys.argv[0][:-3])
