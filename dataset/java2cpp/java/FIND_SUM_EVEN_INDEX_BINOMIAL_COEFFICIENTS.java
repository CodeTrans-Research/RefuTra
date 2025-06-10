int f_gold ( int n ) {
  int C [ ] [ ] = new int [ n + 1 ] [ n + 1 ] ;
  int i , j ;
  for ( i = 0 ;
  i <= n ;
  i ++ ) {
    for ( j = 0 ;
    j <= Math . min ( i , n ) ;
    j ++ ) {
      if ( j == 0 || j == i ) C [ i ] [ j ] = 1 ;
      else C [ i ] [ j ] = C [ i - 1 ] [ j - 1 ] + C [ i - 1 ] [ j ] ;
    }
  }
  int sum = 0 ;
  for ( i = 0 ;
  i <= n ;
  i += 2 ) sum += C [ n ] [ i ] ;
  return sum ;
}