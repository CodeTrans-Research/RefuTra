public static int f_gold (int m, int n, int x) {
    int[][] table = new int[n + 1][x + 1];
    for (int[] row : table) {
        Arrays.fill(row, 0);
    }
    for (int j = 1; j < Math.min(m + 1, x + 1); j++) {
        table[1][j] = 1;
    }
    for (int i = 2; i < n + 1; i++) {
        for (int j = 1; j < x + 1; j++) {
            for (int k = 1; k < Math.min(m + 1, j); k++) {
                table[i][j] += table[i - 1][j - k];
            }
        }
    }
    return table[n][x];
}