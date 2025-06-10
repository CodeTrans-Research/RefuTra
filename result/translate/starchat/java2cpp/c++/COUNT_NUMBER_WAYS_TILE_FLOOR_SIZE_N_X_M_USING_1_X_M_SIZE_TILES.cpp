int f_gold ( int n, int m ) {
    vector <int> count(n+1,0);
    count[0] = 0;
    for (int i = 1; i <= n; i++) {
        if (i > m) count[i] = count[i-1] + count[i-m];
        else if (i < m) count[i] = 1;
        else count[i] = 2;
    }
    return count[n];
}