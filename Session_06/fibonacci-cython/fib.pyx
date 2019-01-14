def fibyf(n):
    """Returns the nth Fibonacci number using Cython loops."""
    cdef int i
    cdef double a = 0, b = 1
    for i in range(n):
        a, b = a+b, a

    return a

def fibyr(n):
    """Returns the nth Fibonacci number using Cython recursions."""
    cdef double r

    if n == 0 or n == 1:
        r = n
    else:
        r = fibyr(n-1)+fibyr(n-2)

    return r
