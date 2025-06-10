int f_gold ( string n ) {
    int dec_value = 0, base = 1;
    for (int i = n.length() - 1; i >= 0; i--) {
        if (n[i] == '1') dec_value += base;
        base *= 2;
    }
    return dec_value;
}