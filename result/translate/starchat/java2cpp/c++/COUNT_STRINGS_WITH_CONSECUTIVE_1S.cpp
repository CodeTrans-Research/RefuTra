int f_gold ( int n ) {
    int *a = new int [n], *b = new int [n];
    a[0] = b[0] = 1;
    for (int i = 1; i < n; i++) {
        a[i] = a[i-1] + b[i-1];
        b[i] = a[i-1];
    }
    int ans = (1 << n) - a[n-1] - b[n-1];
    delete []a;
    delete []b;
    return ans;
}