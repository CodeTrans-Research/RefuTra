public static int f_gold ( int[] ar1, int[] ar2, int n ) {
        int i = 0, j = 0, m1 = -1, m2 = -1, count = 0;
        while ( count < n + 1 ) {
            count++;
            if ( i == n ) {
                m1 = m2;
                m2 = ar2[0];
                break;
            }
            if ( j == n ) {
                m1 = m2;
                m2 = ar1[0];
                break;
            }
            if ( ar1[i] < ar2[j] ) {
                m1 = m2;
                m2 = ar1[i];
                i++;
            } else {
                m1 = m2;
                m2 = ar2[j];
                j++;
            }
        }
        return ( m1 + m2 ) / 2;
    }