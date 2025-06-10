public static int f_gold(int x) {
    if (x == 0 || x == 1) {
        return x;
    }
    int i = 1;
    int result = 1;
    while (result <= x) {
        i += 1;
        result = i * i;
    }
    return i - 1;
}