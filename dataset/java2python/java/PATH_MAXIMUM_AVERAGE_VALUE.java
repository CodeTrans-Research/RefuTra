double f_gold ( int cost [ ] [ ] , int N ) {
  int dp [ ] [ ] = new int [ N + 1 ] [ N + 1 ] ;
  dp [ 0 ] [ 0 ] = cost [ 0 ] [ 0 ] ;
  for ( int i = 1 ;
  i < N ;
  i ++ ) dp [ i ] [ 0 ] = dp [ i - 1 ] [ 0 ] + cost [ i ] [ 0 ] ;
  for ( int j = 1 ;
  j < N ;
  j ++ ) dp [ 0 ] [ j ] = dp [ 0 ] [ j - 1 ] + cost [ 0 ] [ j ] ;
  for ( int i = 1 ;
  i < N ;
  i ++ ) for ( int j = 1 ;
  j < N ;
  j ++ ) dp [ i ] [ j ] = Math . max ( dp [ i - 1 ] [ j ] , dp [ i ] [ j - 1 ] ) + cost [ i ] [ j ] ;
  return ( double ) dp [ N - 1 ] [ N - 1 ] / ( 2 * N - 1 ) ;
}