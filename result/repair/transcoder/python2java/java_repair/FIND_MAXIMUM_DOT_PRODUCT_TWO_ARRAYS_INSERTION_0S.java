  int f_gold ( int [ ] A , int [ ] B , int m , int n ) {
  int [ ] [ ] dp = new int[n+1][m+1];
  for ( int i = 1 ;
  i <= n ;
  i += 1 ) {
    for ( int j = i ;
    j <= m ;
    j += 1 ) {
      dp [ i ] [ j ] = Math . max ( ( dp [ i - 1 ] [ j - 1 ] + ( A [ j - 1 ] * B [ i - 1 ] ) ) , dp [ i ] [ j - 1 ] ) ;
    }
  }
  return dp [ n ] [ m ] ;
}

