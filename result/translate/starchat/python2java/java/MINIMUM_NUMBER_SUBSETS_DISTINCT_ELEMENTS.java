public static int f_gold ( int[] ar, int n ) {
        int res = 0;
        Arrays.sort ( ar );
        int i = 0;
        while ( i < n ) {
            int count = 1;
            int j = i;
            while ( j < n - 1 && ar [ j ] == ar [ j + 1 ] ) {
                count += 1;
                j++;
            }
            i = j;
            res = Math.max ( res, count );
        }
        return res;
    }