bool f_gold ( string s ) {
    for ( int i = 0; i < s.length(); i++) if (!isdigit(s[i])) return false;
    return true;
}