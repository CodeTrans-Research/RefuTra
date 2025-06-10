public static String f_gold(String str1, String str2) {
        if (str1.length() > str2.length()) {
            String temp = str1;
            str1 = str2;
            str2 = temp;
        }
        StringBuilder sb = new StringBuilder();
        int n1 = str1.length();
        int n2 = str2.length();
        str1 = new StringBuilder(str1).reverse().toString();
        str2 = new StringBuilder(str2).reverse().toString();
        int carry = 0;
        for (int i = 0; i < n1; i++) {
            int sum = (str1.charAt(i) - '0' + (str2.charAt(i) - '0' + carry));
            if (sum < 0) {
                sb.append((sum % -10) + '0');
            } else {
                sb.append((sum % 10) + '0');
            }
            carry = sum / 10;
        }
        for (int i = n1; i < n2; i++) {
            int sum = (str2.charAt(i) - '0' + carry);
            if (sum < 0) {
                sb.append((sum % -10) + '0');
            } else {
                sb.append((sum % 10) + '0');
            }
            carry = sum / 10;
        }
        if (carry > 0) {
            sb.append(carry + '0');
        }
        return new StringBuilder(sb).reverse().toString();
    }