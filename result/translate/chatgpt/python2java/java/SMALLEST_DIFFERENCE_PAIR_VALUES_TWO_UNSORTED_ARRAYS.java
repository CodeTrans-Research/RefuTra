public static int f_gold(int[] A, int[] B, int m, int n) {
    Arrays.sort(A, 0, m);
    Arrays.sort(B, 0, n);
    int a = 0;
    int b = 0;
    int result = Integer.MAX_VALUE;
    while (a < m && b < n) {
        if (Math.abs(A[a] - B[b]) < result) {
            result = Math.abs(A[a] - B[b]);
        }
        if (A[a] < B[b]) {
            a += 1;
        } else {
            b += 1;
        }
    }
    return result;
}