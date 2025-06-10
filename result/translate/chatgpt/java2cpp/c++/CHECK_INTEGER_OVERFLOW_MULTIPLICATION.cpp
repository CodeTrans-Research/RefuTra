bool f_gold(long a, long b) {
    if (a == 0 || b == 0) {
        return false;
    }
    long result = a * b;
    if (a == result / b) {
        return false;
    } else {
        return true;
    }
}