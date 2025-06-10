public static int f_gold ( int n ) {
        int ans = 0, i = 0;
        while ( ( 1 << i ) <= n ) {
            int k = 0;
            int change = 1 << i;
            for ( int j = 0; j <= n; j++ ) {
                ans += k;
                if ( change == 1 ) {
                    k = 1 - k;
                    change = 1 << i;
                } else {
                    change--;
                }
            }
            i++;
        }
        return ans;
    }