void f_gold ( int arr [ ] , int n ) {
  Vector < Integer > evenArr = new Vector < Integer > ( ) ;
  Vector < Integer > oddArr = new Vector < Integer > ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( i % 2 != 1 ) {
      evenArr . add ( arr [ i ] ) ;
    }
    else {
      oddArr . add ( arr [ i ] ) ;
    }
  }
  Collections . sort ( evenArr ) ;
  Collections . sort ( oddArr , Collections . reverseOrder ( ) ) ;
  int i = 0 ;
  for ( int j = 0 ;
  j < evenArr . size ( ) ;
  j ++ ) {
    arr [ i ++ ] = evenArr . get ( j ) ;
  }
  for ( int j = 0 ;
  j < oddArr . size ( ) ;
  j ++ ) {
    arr [ i ++ ] = oddArr . get ( j ) ;
  }
}