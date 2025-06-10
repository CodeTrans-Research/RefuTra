string f_gold ( string str1, string str2 ) {
        if (str1.length() > str2.length()) {
            string t = str1;
            str1 = str2;
            str2 = t;
        }
        string str = "";
        int n1 = str1.length(), n2 = str2.length();
        str1 = reverse(str1);
        str2 = reverse(str2);
        int carry = 0;
        for (int i = 0; i < n1; i++) {
            int sum = ((int) (str1[i] - '0') + (int) (str2[i] - '0') + carry);
            str += (char) (sum % 10 + '0');
            carry = sum / 10;
        }
        for (int i = n1; i < n2; i++) {
            int sum = ((int) (str2[i] - '0') + carry);
            str += (char) (sum % 10 + '0');
            carry = sum / 10;
        }
        if (carry != 0) str += (char) (carry + '0');
        return reverse(str);
    }