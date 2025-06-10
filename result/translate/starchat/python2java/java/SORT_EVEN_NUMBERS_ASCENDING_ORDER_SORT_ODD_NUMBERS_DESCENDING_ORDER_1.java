public static void f_gold ( int arr [ ], int n ) {
        for ( int i = 0; i < n; i++) {
            if ((arr[i] & 1) == 1) {
                arr[i] = -arr[i];
            }
        }
        Arrays.sort(arr);
        for ( int i = 0; i < n; i++) {
            if ((arr[i] & 1) == 1) {
                arr[i] = -arr[i];
            }
        }
    }