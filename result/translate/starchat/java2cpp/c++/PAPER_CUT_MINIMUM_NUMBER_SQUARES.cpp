int f_gold ( int a, int b ) {
    if (a < b) {
        int temp = a;
        a = b;
        b = temp;
    }
    int res = 0;
    while (b > 0) {
        res += a / b;
        int rem = a % b;
        a = b;
        b = rem;
    }
    return res;
}