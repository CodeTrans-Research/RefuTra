public static int f_gold ( int n ) {
        int count = 0;
        for ( int curr = 0; ; curr++ ) {
            int sum = 0;
            int x = curr;
            while ( x!= 0 ) {
                sum += x % 10;
                x /= 10;
            }
            if ( sum == 10 ) {
                count++;
                if ( count == n ) {
                    return curr;
                }
            }
        }
        return -1;
    }