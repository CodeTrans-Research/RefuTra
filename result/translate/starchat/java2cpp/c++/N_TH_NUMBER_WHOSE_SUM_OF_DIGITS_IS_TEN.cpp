int f_gold ( int n ) {
    int count = 0 ;
    for ( int curr = 1 ; curr <= 1000000 ; curr ++ ) {
        int sum = 0 ;
        for ( int x = curr ; x > 0 ; x = x / 10 ) sum = sum + x % 10 ;
        if ( sum == 10 ) count ++ ;
        if ( count == n ) return curr ;
    }
}