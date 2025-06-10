public static int f_gold ( int[] a, int n ) {
        Arrays.sort ( a );
        int sum = 0, len = 0, i = 0;
        boolean flag = false;
        while ( i < n - 1 ) {
            if ( ( a [ i ] == a [ i + 1 ] && flag == false ) || ( a [ i ] - a [ i + 1 ] == 1 && flag == false ) ) {
                flag = true;
                len = a [ i + 1 ];
                i++;
            } else if ( flag == true ) {
                sum += a [ i + 1 ] * len;
                flag = false;
                i++;
            } else {
                i++;
            }
        }
        return sum;
    }