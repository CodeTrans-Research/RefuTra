int f_gold ( int n ) {
    vector<vector<int>> a(n + 1, vector<int>(10, 0));
    for (int i = 0; i <= 9; i++) a[0][i] = 1;
    for (int i = 1; i <= n; i++) a[i][9] = 1;
    for (int i = 1; i <= n; i++)
        for (int j = 8; j >= 0; j--)
            a[i][j] = a[i - 1][j] + a[i][j + 1];
    return a[n][0];
}