public static int f_gold ( String s ) {
        int _sum = 0, n = 1;
        while ( _sum < s.length() ) {
            _sum += n * n;
            n += 1;
        }
        n -= 1;
        if ( _sum == s.length() ) return n;
        return -1;
    }