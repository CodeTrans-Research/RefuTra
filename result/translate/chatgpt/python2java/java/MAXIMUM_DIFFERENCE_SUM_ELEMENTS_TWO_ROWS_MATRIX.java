public static int f_gold(int[][] mat, int m, int n) {
    int[] rowSum = new int[m];
    for (int i = 0; i < m; i++) {
        int sum = 0;
        for (int j = 0; j < n; j++) {
            sum += mat[i][j];
        }
        rowSum[i] = sum;
    }
    int max_diff = rowSum[1] - rowSum[0];
    int min_element = rowSum[0];
    for (int i = 1; i < m; i++) {
        if (rowSum[i] - min_element > max_diff) {
            max_diff = rowSum[i] - min_element;
        }
        if (rowSum[i] < min_element) {
            min_element = rowSum[i];
        }
    }
    return max_diff;
}