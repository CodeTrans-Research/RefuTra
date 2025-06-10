public static int f_gold(int[] arr, int n) {
    int min_xor = 999999;
    int val = 0;

    for(int i = 0; i < n; i++) {
        for(int j = i + 1; j < n; j++) {
            val = arr[i] ^ arr[j];
            min_xor = Math.min(min_xor, val);
        }
    }

    return min_xor;
}