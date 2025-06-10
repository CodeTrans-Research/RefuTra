int f_gold(int x, int p1, int p2, int n) {
    int set1 = (x >> p1) & ((1 << n) - 1);
    int set2 = (x >> p2) & ((1 << n) - 1);
    int xor_val = (set1 ^ set2);
    xor_val = (xor_val << p1) | (xor_val << p2);
    int result = x ^ xor_val;
    return result;
}