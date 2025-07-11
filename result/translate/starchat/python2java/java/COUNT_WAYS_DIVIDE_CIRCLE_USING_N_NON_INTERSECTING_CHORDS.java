public static int f_gold ( int A ) {
        int n = 2 * A;
        int[] dpArray = new int[n + 1];
        dpArray[0] = 1;
        dpArray[2] = 1;
        for ( int i = 4; i <= n; i += 2 ) {
            for ( int j = 0; j < i - 2; j += 2 ) {
                dpArray[i] += dpArray[j] * dpArray[i - 2 - j];
            }
        }
        return (int) Math.floor(dpArray[n]);
    }