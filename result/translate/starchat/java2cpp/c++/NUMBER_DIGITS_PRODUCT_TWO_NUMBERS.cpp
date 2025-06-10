int f_gold ( int a, int b ) {
    int count = 0, p = abs(a * b);
    while (p) {
        count++;
        p /= 10;
    }
    return count;
}