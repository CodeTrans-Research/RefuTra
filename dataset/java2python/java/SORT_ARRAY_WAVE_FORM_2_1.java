void f_gold ( int arr [ ] , int n ) {
  for ( int i = 0 ;
  i < n ;
  i += 2 ) {
    if ( i > 0 && arr [ i - 1 ] > arr [ i ] ) swap ( arr , i - 1 , i ) ;
    if ( i < n - 1 && arr [ i ] < arr [ i + 1 ] ) swap ( arr , i , i + 1 ) ;
  }
}