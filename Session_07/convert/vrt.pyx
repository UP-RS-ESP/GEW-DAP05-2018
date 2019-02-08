import numpy as np

cdef extern from "cvrt.c":
    void cvrt(int *out, const double *src, const unsigned int n)

def vrtc(const double[:,:] src):
    cdef int[:, ::1] mv
    cdef unsigned int i, k, n, m

    m, n = src.shape[0], src.shape[1]
    out = np.zeros((m, n), dtype = np.int32)
    mv = out
    cvrt(&mv[0,0], &src[0,0], m*n)
    return out

def vrty(const double[:,:] src):
    cdef int[:, ::1] mv
    cdef unsigned int i, k, n, m

    m, n = src.shape[0], src.shape[1]
    out = np.zeros((m, n), dtype = np.int32)
    mv = out
    for i in range(m):
        for k in range(n):
            mv[i, k] = int(src[i, k] + n * i + k)

    return out

def vrty_naive(const double[:,:] src):
    cdef unsigned int i, k, n, m

    m, n = src.shape[0], src.shape[1]
    out = np.zeros((m, n), dtype = np.int32)
    for i in range(m):
        for k in range(n):
            out[i, k] = int(src[i, k] + n * i + k)

    return out
