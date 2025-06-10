int f_gold ( int arr [ ] [ ], int n ) {
    int diff = INT_MAX;
    for (int i = 0; i < n - 1; i++) {
        if (arr[i + 1][0] - arr[i][0] < diff) diff = arr[ i + 1 ][0] - arr[i][0];
    }
    return diff;    
}