int f_gold ( int A [ ], int n ) {
    int min_val = *min_element(A, A+n);
    return min_val * (n - 1);
}