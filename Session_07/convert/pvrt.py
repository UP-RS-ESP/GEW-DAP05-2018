import numpy as np

def vrty_naive(src):
    m, n = src.shape[0], src.shape[1]
    out = np.zeros((m, n), dtype = np.int32)
    for i in range(m):
        for k in range(n):
            out[i, k] = src[i, k] + n * i + k

    return out
