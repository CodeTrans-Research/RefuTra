int f_gold(int n) {
    if (n == 0) return 1;
    return n * f_gold(n - 1);
}