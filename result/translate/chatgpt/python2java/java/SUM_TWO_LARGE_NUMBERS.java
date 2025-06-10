public String f_gold(String str1, String str2) {
    if (str1.length() > str2.length()) {
        String t = str1;
        str1 = str2;
        str2 = t;
    }
    String str = "";
    int n1 = str1.length();
    int n2 = str2.length();
    str1 = new StringBuilder(str1).reverse().toString();
    str2 = new StringBuilder(str2).reverse().toString();
    int carry = 0;
    for (int i = 0; i < n1; i++) {
        int sum = ((int)str1.charAt(i) - 48) + ((int)str2.charAt(i) - 48) + carry;
        if (sum < 0) {
            str += (char)(sum % -10 + 48);
        } else {
            str += (char)(sum % 10 + 48);
        }
        carry = (int)sum / 10;
    }
    for (int i = n1; i < n2; i++) {
        int sum = ((int)str2.charAt(i) - 48) + carry;
        if (sum < 0) {
            str += (char)(sum % -10 + 48);
        } else {
            str += (char)(sum % 10 + 48);
        }
        carry = (int)sum / 10;
    }
    if (carry != 0) {
        str += (char)(carry + 48);
    }
    str = new StringBuilder(str).reverse().toString();
    return str;
}