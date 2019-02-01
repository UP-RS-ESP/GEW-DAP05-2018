cdef extern from "cmog.c":
    void cmog(double *arr, const unsigned int n)

def mogc(double[:] arr):
    return cmog(&arr[0], arr.shape[0])

def mogy(double[:] arr):
    cdef unsigned int i, n
    n = arr.shape[0]
    for i in range(n):
        arr[i] = i

def moggy(arr):
    n = arr.shape[0]
    for i in range(n):
        arr[i] = i
