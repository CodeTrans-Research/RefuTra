public static int f_gold ( int n ) {
        int ans = 0;
        for ( int length = 1 ; length <= (int) Math.sqrt ( n ) ; length++ ) {
            int height = length;
            while ( height * length <= n ) {
                ans++;
                height++;
            }
        }
        return ans;
    }