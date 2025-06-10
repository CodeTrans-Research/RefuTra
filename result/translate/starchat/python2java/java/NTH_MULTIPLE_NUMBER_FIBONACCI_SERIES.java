public static int f_gold( int k, int n ) {
        int f1 = 0, f2 = 1, i = 2;
        while ( i!= 0 ) {
            int f3 = f1 + f2;
            f1 = f2;
            f2 = f3;
            if ( f2 % k == 0 ) return n * i;
            i++;
        }
        return 0;
    }