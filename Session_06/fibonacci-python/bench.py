import numpy as np

def fibf(n):
    a = 0.0
    b = 1.0
    for i in range(n):
        a, b = a+b, a

    return a

def fibr(n):
    if n == 0 or n == 1:
        a = n
    else:
        a = fibr(n-1)+fibr(n-2)

    return a

def main():
    import sys
    from timeit import timeit
    from matplotlib import pyplot as pl

    number = 10000
    m = 15

    tpr = np.zeros(m)
    tpf = np.zeros(m)
    for i in range(m):
        tpr[i] = timeit('fibr(%i)' % i,
                 setup = 'from __main__ import fibr', number = number) / number
        tpf[i] = timeit('fibf(%i)' % i,
                 setup = 'from __main__ import fibf', number = number) / number

    pl.figure(1, (10.24, 7.68))
    pl.title('Fibonacci benchmark')
    pl.semilogy(tpr, label = 'Python recursion')
    pl.semilogy(tpf, label = 'Python for loop')
    pl.xlabel('Interation / Fibonacci number')
    pl.ylabel('Time [s]')
    pl.legend(loc = 'upper left')
    pl.show()

if __name__ == '__main__':
    main()

