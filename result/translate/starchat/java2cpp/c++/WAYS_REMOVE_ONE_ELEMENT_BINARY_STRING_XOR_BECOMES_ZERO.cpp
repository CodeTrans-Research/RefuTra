int f_gold ( string s ) {
    int one_count = 0, zero_count = 0;
    for (int i = 0; i < s.length(); i++) {
        if (s[i] == '1') one_count++;
        else zero_count++;
    }
    if (one_count % 2 == 0) return zero_count;
    return one_count;
}