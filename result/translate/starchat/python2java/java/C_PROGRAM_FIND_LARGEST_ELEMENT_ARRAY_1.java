public static int f_gold ( int[] arr, int n ) {
        return Arrays.stream(arr, 0, n).max().getAsInt();
    }