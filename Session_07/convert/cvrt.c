void
cvrt(int *out, const double *src, const unsigned int n) {
    unsigned int i;

    for(i = 0; i < n; i++)
        out[i] = src[i] + i;
}
