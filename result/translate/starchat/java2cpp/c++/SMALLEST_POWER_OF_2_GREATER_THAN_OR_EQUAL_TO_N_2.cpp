int f_gold ( int n ) {
    int res = 0;
    while (n) {
        res |= n & (-n);
        n = n ^ (n & (-n));
    }
    return res + 1;
}