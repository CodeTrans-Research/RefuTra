int f_gold ( int a [ ], int n ) {
    set < int > s;
    for ( int i = 0; i < n; i++) s.insert (a[i]);
    int arr_sum = accumulate (a, a + n, 0);
    int set_sum = accumulate (s.begin(), s.end(), 0);
    return ( 3 * set_sum - arr_sum ) / 2;
}