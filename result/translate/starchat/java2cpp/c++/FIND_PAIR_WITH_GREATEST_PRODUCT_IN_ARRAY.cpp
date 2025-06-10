int f_gold ( int arr [ ] [ ] A, int n ) {
    int result = -1;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n - 1; j++) {
            for (int k = j + 1; k < n; k++) {
                if (A[j][0] * A[k][1] == A[i][1]) {
                    result = max(result, A[i][0]);
                }
            }
        }
    }
    return result;
}