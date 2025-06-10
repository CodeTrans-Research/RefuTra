public int f_gold(int s) {
    int _sum = 0;
    int n = 1;
    while (_sum < s) {
        _sum += n * n;
        n += 1;
    }
    n -= 1;
    if (_sum == s) {
        return n;
    }
    return -1;
}