int f_gold ( int a, int b ) {
    if (a == 0) return b;
    return f_gold(b % a, a);
}