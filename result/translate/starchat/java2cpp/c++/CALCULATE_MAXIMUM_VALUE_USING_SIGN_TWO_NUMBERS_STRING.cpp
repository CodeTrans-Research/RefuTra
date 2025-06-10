int f_gold ( string str ) {
    int res = (int)str[0] - '0';
    for ( int i = 1; i < str.length(); i++ ) {
        if ( str[i] == '0' || str[i] == '1' || res < 2 ) res += (int)str[i] - '0';
        else res = res * 10 + (int)str[i] - '0';
    }
    return res;
}