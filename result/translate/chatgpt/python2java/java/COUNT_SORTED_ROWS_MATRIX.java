public int f_gold(int[][] mat, int r, int c) {
    int result = 0;
    for (int i = 0; i < r; i++) {
        int j = 0;
        for (j = 0; j < c - 1; j++) {
            if (mat[i][j + 1] <= mat[i][j]) {
                break;
            }
        }
        if (j == c - 1) {
            result += 1;
        }
    }
    for (int i = 0; i < r; i++) {
        int j = 0;
        for (j = c - 1; j > 0; j--) {
            if (mat[i][j - 1] <= mat[i][j]) {
                break;
            }
        }
        if (c > 1 && j == 1) {
            result += 1;
        }
    }
    return result;
}