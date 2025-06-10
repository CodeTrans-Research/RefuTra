std::string f_gold(std::string str1, std::string str2) {
    if (str1.length() > str2.length()) {
        std::string t = str1;
        str1 = str2;
        str2 = t;
    }
    std::string str = "";
    int n1 = str1.length(), n2 = str2.length();
    str1 = std::string(str1.rbegin(), str1.rend());
    str2 = std::string(str2.rbegin(), str2.rend());
    int carry = 0;
    for (int i = 0; i < n1; i++) {
        int sum = (int)(str1[i] - '0') + (int)(str2[i] - '0') + carry;
        str += (char)(sum % 10 + '0');
        carry = sum / 10;
    }
    for (int i = n1; i < n2; i++) {
        int sum = (int)(str2[i] - '0') + carry;
        str += (char)(sum % 10 + '0');
        carry = sum / 10;
    }
    if (carry != 0) str += (char)(carry + '0');
    str = std::string(str.rbegin(), str.rend());
    return str;
}