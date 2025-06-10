public static int f_gold ( String str, int n ) {
        int ans = ( n * ( n + 1 ) ) / 2;
        int a_index = 0, b_index = 0, c_index = 0;
        for ( int i = 0; i < n; i++ ) {
            if ( str.charAt(i) == 'a' ) {
                a_index = i + 1;
                ans -= Math.min(b_index, c_index);
            }
            else if ( str.charAt(i) == 'b' ) {
                b_index = i + 1;
                ans -= Math.min(a_index, c_index);
            }
            else {
                c_index = i + 1;
                ans -= Math.min(a_index, b_index);
            }
        }
        return ans;
    }