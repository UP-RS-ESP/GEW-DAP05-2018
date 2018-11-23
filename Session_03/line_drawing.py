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
    
    x = np.append(np.arange(x0, x1, wx), [x1,])
    y = np.append(np.arange(y0, y1, wy), [y1,])

    return (y.astype('int'), x.astype('int'))

#np.random.seed(18762343)
w = float(sys.argv[1])

xb = np.arange(-2, 2+w, w)
yb = np.arange(-1, 1+w, w)
z = np.zeros((len(yb), len(xb)))

pts = np.random.random((4, 2))
pts[:, 0] *= 2
for i in range(pts.shape[0]):
    for k in range(i):
        yl, xl = draw_line(pts[i,:], pts[k,:], xb, yb)
        pl.plot(pts[(i,k),0], pts[(i,k),1], 'ro-',
                markersize = 11,
                markerfacecolor = 'none',
                markeredgewidth = 1)
        z[yl, xl] += 1

pts = np.random.random((3, 2)) - 1
pts[:, 0] *= 2
for i in range(pts.shape[0]):
    for k in range(i):
        yl, xl = draw_line(pts[i], pts[k], xb, yb)
        pl.plot(pts[(i,k),0], pts[(i,k),1], 'yo-',
                markersize = 11,
                markerfacecolor = 'none',
                markeredgewidth = 1)
        z[yl, xl] += 1

pl.pcolormesh(xb, yb, z, alpha = 0.8)
ax = pl.gca()
ax.set_aspect('equal')
pl.show()
