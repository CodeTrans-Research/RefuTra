public static int f_gold ( int n ) {
  int [ ] [ ] arr = new int [ n ] [ n ] ;
  for ( int y = 0 ;
  y < n ;
  y ++ ) {
    arr [ y ] [ 0 ] = 0 ;
    arr [ y ] [ 1 ] = 0 ;
    arr [ y ] [ 2 ] = 0 ;
    arr [ y ] [ 3 ] = 0 ;
  }
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    for ( int j = 0 ;
    j < n ;
    j ++ ) {
      arr [ i ] [ j ] = Math . abs ( i - j ) ;
    }
  }
  int sum = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    for ( int j = 0 ;
    j < n ;
    j ++ ) {
      sum += arr [ i ] [ j ] ;
    }
  }
  return sum ;
}
