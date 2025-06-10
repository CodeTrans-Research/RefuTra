public static int f_gold(String str) {
    int one_count = 0;
    int zero_count = 0;
    int n = str.length();
    for(int i = 0; i < n; i++) {
        if(str.charAt(i) == '1') {
            one_count += 1;
        } else {
            zero_count += 1;
        }
    }
    if(one_count % 2 == 0) {
        return zero_count;
    }
    return one_count;
}