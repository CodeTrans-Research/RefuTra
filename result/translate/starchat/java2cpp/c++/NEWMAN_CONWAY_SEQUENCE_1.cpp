int f_gold ( int n ) {
    vector <int> f(n+1);
    f[0] = 0;
    f[1] = 1;
    f[2] = 1;
    for (int i = 3; i <= n; i++) f[i] = f[i-1] + f[i-f[i-1]];
    return f[n];
}