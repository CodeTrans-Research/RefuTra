int f_gold ( int [ ] arr , int n ) {
  HashMap < Integer , Indexes > map = new HashMap < > ( ) ;
  for ( int i = 0 ;
  i < n - 1 ;
  i ++ ) {
    for ( int j = i + 1 ;
    j < n ;
    j ++ ) {
      map . put ( arr [ i ] + arr [ j ] , new Indexes ( i , j ) ) ;
    }
  }
  int d = Integer . MIN_VALUE ;
  for ( int i = 0 ;
  i < n - 1 ;
  i ++ ) {
    for ( int j = i + 1 ;
    j < n ;
    j ++ ) {
      int abs_diff = Math . abs ( arr [ i ] - arr [ j ] ) ;
      if ( map . containsKey ( abs_diff ) ) {
        Indexes indexes = map . get ( abs_diff ) ;
        if ( indexes . getI ( ) != i && indexes . getI ( ) != j && indexes . getJ ( ) != i && indexes . getJ ( ) != j ) {
          d = Math . max ( d , Math . max ( arr [ i ] , arr [ j ] ) ) ;
        }
      }
    }
  }
  return d ;
}