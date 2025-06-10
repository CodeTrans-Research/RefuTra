public static boolean f_gold ( String num ) {
    int n = num. length ( );
    if ( n == 0 && num. equals ( "\n" ) ) return true;
    if ( n % 3 == 1 ) num = num + "00";
    else if ( n % 3 == 2 ) num = num + "0";
    int GSum = 0, p = 1;
    for ( int i = n - 1; i >= 0; i-- ) {
        int group = num. charAt ( i ) - '0';
        if ( i > 0 ) group = group * 10 + num. charAt ( i - 1 ) - '0';
        if ( i > 1 ) group = group * 10 + num. charAt ( i - 2 ) - '0';
        GSum += group * p;
        p *= -1;
    }
    return GSum % 7 == 0;
}