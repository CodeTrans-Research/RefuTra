boolean f_gold (int n, int i) {
    if (n <= 2) {
        return n == 2 ? true : false;
    }
    if (n % i == 0) {
        return false;
    }
    if (i * i > n) {
        return true;
    }
    return f_gold(n, i + 1);
}