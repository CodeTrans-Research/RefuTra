public static boolean f_gold(int[][] mat , int n) {
    int diag1_left = 0;
    int diag1_right = 0;
    int diag2_left = 0;
    int diag2_right = 0;
    int i = 0;
    int j = n - 1;
    while (i < n) {
        if (i < n / 2) {
            diag1_left += mat[i][i];
            diag2_left += mat[j][i];
        } else if (i > n / 2) {
            diag1_right += mat[i][i];
            diag2_right += mat[j][i];
        }
        i += 1;
        j -= 1;
    }
    return (diag1_left == diag2_right && diag2_right == diag2_left &&
            diag1_right == diag2_left && diag2_right == mat[n / 2][n / 2]);
}