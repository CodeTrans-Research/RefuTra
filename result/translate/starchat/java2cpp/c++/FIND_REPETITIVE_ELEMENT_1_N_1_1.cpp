int f_gold ( int arr [ ], int n ) {
    set < int > s;
    for ( int i = 0 ; i < n ; i ++ ) {
        if ( s.find(arr[i])!= s.end() ) return arr[i];
        s.insert(arr[i]);
    }
    return -1;
}