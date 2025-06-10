void f_gold ( int arr [ ] [ ] arr_2d, int n, int m ) {
    for ( int i = 0; i < n; i++ ) {
        for ( int j = 0; j < m; j++ ) {
            arr_2d [ i ] [ j ] = i * m + j + 1;
        }
    }
}