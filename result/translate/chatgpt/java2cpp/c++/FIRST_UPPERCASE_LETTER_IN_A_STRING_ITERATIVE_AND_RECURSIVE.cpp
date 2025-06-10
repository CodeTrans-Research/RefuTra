char f_gold(string str) {
    for (int i = 0; i < str.length(); i++) {
        if (isupper(str[i])) {
            return str[i];
        }
    }
    return 0;
}