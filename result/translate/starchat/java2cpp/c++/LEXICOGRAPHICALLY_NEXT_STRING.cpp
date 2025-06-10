string f_gold ( string str ) {
    if (str.empty()) return "a";
    int i = str.length() - 1;
    while (str[i] == 'z' && i >= 0) i--;
    if (i == -1) str = str + 'a';
    else str = str.substr(0, i) + (char)((int)(str[i]) + 1) + str.substr(i + 1);
    return str;
}