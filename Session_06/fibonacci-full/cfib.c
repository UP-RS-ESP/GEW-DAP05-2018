unsigned int
cfibr(int n) {
    unsigned int r;

    if(n == 0 || n == 1)
        r = n;
    else
        r = cfibr(n-1) + cfibr(n-2);

    return r;
}

unsigned int
cfibf(int n) {
    int i;
    unsigned int a, b, c;

    a = 0;
    b = 1;
    c = 0;

    for(i = 0; i < n; i++) {
        c = a + b;
        a = b;
        b = c;
    }

    return c;
}
