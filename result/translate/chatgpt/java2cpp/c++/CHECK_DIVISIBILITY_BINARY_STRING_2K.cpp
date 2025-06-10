bool f_gold(string str, int k) {
    int n = str.length();
    int c = 0;
    for (int i = 0; i < k; i++) {
        if (str[n - i - 1] == '0') {
            c++;
        }
    }
    return (c == k);
}