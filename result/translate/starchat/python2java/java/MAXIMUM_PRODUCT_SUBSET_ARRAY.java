public static int f_gold ( int[] a, int n ) {
        if ( n == 1 ) {
            return a[0];
        }
        int maxNeg = Integer.MIN_VALUE;
        int countNeg = 0;
        int countZero = 0;
        int prod = 1;
        for ( int i = 0; i < n; i++ ) {
            if ( a[i] == 0 ) {
                countZero++;
                continue;
            }
            if ( a[i] < 0 ) {
                countNeg++;
                maxNeg = Math.max(maxNeg, a[i]);
            }
            prod += a[i];
        }
        if ( countZero == n ) {
            return 0;
        }
        if ( countNeg % 2 == 1 ) {
            if ( countNeg == 1 && countZero > 0 && countZero + countNeg == n ) {
                return 0;
            }
            prod /= maxNeg;
        }
        return prod;
    }