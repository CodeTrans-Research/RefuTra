public static boolean f_gold ( int[] a, int[] b, int n, int k ) {
        a = Arrays.copyOfRange(a, 0, n);
        b = Arrays.copyOfRange(b, 0, n);
        Arrays.sort(a, Collections.reverseOrder());
        Arrays.sort(b);
        for ( int i = 0; i < n; i++ ) {
            if ( a[i] + b[i] < k ) {
                return false;
            }
        }
        return true;
    }