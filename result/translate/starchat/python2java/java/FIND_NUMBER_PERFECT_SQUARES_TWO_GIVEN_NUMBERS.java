public static int f_gold ( int a, int b ) {
        int cnt = 0;
        for ( int i = a ; i <= b ; i++ ) {
            int j = 1;
            while ( j * j <= i ) {
                if ( j * j == i ) {
                    cnt++;
                }
                j++;
            }
        }
        return cnt;
    }