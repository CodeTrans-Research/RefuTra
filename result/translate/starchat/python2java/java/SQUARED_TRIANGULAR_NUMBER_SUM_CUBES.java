public static int f_gold ( String s ) {
        int _sum = 0, n = 1;
        while ( _sum < s. charAt ( 0 ) - '0' ) {
            _sum += n * n * n;
            n++;
        }
        return ( _sum == s. charAt ( 0 ) - '0' )? n - 1 : - 1;
    }