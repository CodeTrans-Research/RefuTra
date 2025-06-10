bool f_gold ( string str ) {
    int l = 0, h = str.length() - 1;
    while (l < h) if (str[l++]!= str[h--]) return false;
    return true;
}