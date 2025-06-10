public static int f_gold(String num) {
    int dec_value = 0;
    int base1 = 1;
    int len1 = num.length();
    
    for (int i = len1 - 1; i >= 0; i--) {
        if (num.charAt(i) == '1') {
            dec_value += base1;
        }
        base1 = base1 * 2;
    }
    
    return dec_value;
}