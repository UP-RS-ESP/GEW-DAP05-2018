---
title: Fractal dimension estimation using box counting
author: Aljoscha Rheinwalt
date: 2018-12-07
---

# Abstract

Numerical estimations of fractal dimensions is key in
studies of data where the dimension can not be derived
mathematically. Here, I present a Python implementation of
the most common estimation technique of box counting, and
analyze its performance for the dimension estimation of the
Koch curve where the fractal dimension can be derived
analytically.

# Koch curve

The Koch curve is one of the earliest fractal curves that have been described. It is based on the Koch curve, which appeared in a 1904 paper titled "On a continuous curve without tangents, constructible from elementary geometry" by the Swedish mathematician Helge von Koch.

![Iterative Koch curve construction depicted by the first steps from order 0 to the 4th order. \label{fig:kochcurve}](kochcurve.pdf)

# Box counting

# Python implementation


~~~~~~~~~~~~~~~~~ {.python .numberLines}
def koch(x0, y0, rho, phi, order):
    global xtrace, ytrace

    x1, y1 = x0 + rho * np.cos(phi), y0 + rho * np.sin(phi)
    if order:
        x, y = x0, y0
        for angle in [0, np.pi/3, 5*np.pi/3, 0]:
            x, y = koch(x, y, rho / 3.0, phi + angle, order - 1)
    else:
        xtrace.append(x1)
        ytrace.append(y1)

    return (x1, y1)

~~~~~~~~~~~~~~~~~

![Power-law regression of .. \label{fig:kochdim}](kochdim.pdf)

# Conclusion

This study of the Koch curve and its fractal dimension .. (see Fig. \ref{fig:kochdim}).
