cdef extern from "cfib.c":
    unsigned int cfibf(int n)
    unsigned int cfibr(int n)

def fibcf(n):
    """Returns the nth Fibonacci number using C loops."""
    return cfibf(n)

def fibcr(n):
    """Returns the nth Fibonacci number using C recursion."""
    return cfibr(n)

def fibyf(int n):
    """Returns the nth Fibonacci number using Cython loops."""
    cdef int i
    cdef int a = 0, b = 1
    for i in range(n):
        a, b = a+b, a

    return a

def fibyr(int n):
    """Returns the nth Fibonacci number using Cython recursions."""
    cdef int r

    if n == 0 or n == 1:
        r = n
    else:
        r = fibyr(n-1)+fibyr(n-2)

    return r

