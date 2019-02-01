cdef extern from "mfd.c":
void mfdtda(double *tda, const double *z,
            const int xlen, const int ylen,
            const double w, const double ppexp);

def tda(double[:,:] dem, double cellwidth, double pexp = 1.1):
    tda = np.zeros(dem.shape)
    #cmog(&arr[0], arr.shape[0])
    return tda

#def sca(double[:,:] dem, double cellwidth):
