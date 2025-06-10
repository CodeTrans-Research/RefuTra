int f_gold ( int n ) {
    vector <int> table (n + 1, 0);
    for (int i = 0; i <= n; i++) table[i] = 1;
    for (int i = 1; i < n; i++) {
        for (int j = i; j <= n; j++) table[j] += table[j - i];
    }
    return table[n];
}