public static int f_gold ( int[] a, int n ) {
        int i = 0, total = 1;
        for ( i = 2; i <= n + 2; i++ ) {
            total += i;
            total -= a[i - 2];
        }
        return total;
    }