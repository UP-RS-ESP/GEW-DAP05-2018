import numpy as np

cdef extern from "cmfd.c":
    void mfdtda(double *a, const double *z,
        const int xlen, const int ylen,
        const double w, const double ppexp);

def sca(const double[:,:] dem, const double cellwidth, const double pexp = 1.1):
    """
    hallo
    """
    cdef double[:, :] mv
    cdef unsigned int n, m

    n, m = dem.shape[0], dem.shape[1]
    out = np.zeros((n, m))
    mv = out
    mfdtda(&mv[0,0], &dem[0,0],
            m, n, cellwidth, pexp)
    out /= cellwidth
    return out

