int f_gold ( int n , int m ) {
  vector < vector < int >> dp ( m + 1 , vector < int > ( n + 1 , 0 ) ) ;
  for ( int i = 0 ;
  i <= m ;
  i ++ ) {
    dp [ i ] [ 0 ] = 1 ;
  }
  for ( int i = 0 ;
  i <= m ;
  i ++ ) {
    dp [ 0 ] [ i ] = 1 ;
  }
  for ( int i = 1 ;
  i <= m ;
  i ++ ) for ( int j = 1 ;
  j <= n ;
  j ++ ) dp [ i ] [ j ] = dp [ i - 1 ] [ j ] + dp [ i - 1 ] [ j - 1 ] + dp [ i ] [ j - 1 ] ;
  return dp [ m ] [ n ] ;
}