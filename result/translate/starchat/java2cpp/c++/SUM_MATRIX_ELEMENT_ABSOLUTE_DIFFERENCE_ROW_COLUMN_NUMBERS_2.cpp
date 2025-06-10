int f_gold ( int n ) {
    int sum = 0;
    for (int i = 1; i <= n; i++) {
        sum += i * (i + 1) / 2;
        sum += i * (i + 1) * (2 * i + 1) / 6;
    }
    return sum;
}