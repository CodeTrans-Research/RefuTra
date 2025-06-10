bool f_gold ( string str ) {
    vector <bool> mark(26, false);
    int index = 0;
    for (int i = 0; i < str.length(); i++) {
        if (str[i] >= 'A' && str[i] <= 'Z') index = str[i] - 'A';
        else if (str[i] >= 'a' && str[i] <= 'z') index = str[i] - 'a';
        mark[index] = true;
    }
    for (int i = 0; i <= 25; i++) if (mark[i] == false) return false;
    return true;
}