int f_gold ( int m, int n ) {
  int count [ ] [ ] = new int [ m ] [ n ] ;
  for ( int i = 0 ; i < m ; i ++ ) {
    for ( int j = 0 ; j < n ; j ++ ) {
      if ( i == 0 || j == 0 ) count [ i ] [ j ] = 1 ;
      else count [ i ] [ j ] = count [ i - 1 ] [ j ] + count [ i ] [ j - 1 ] ;
    }
  }
  return count [ m - 1 ] [ n - 1 ] ;
}