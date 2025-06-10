public static int f_gold ( int N ) {
  int [ ] dp = new int [ N ] ;
  dp [ 0 ] = 1 ;
  dp [ 1 ] = 2 ;
  int i = 1 ;
  while ( dp [ i ] <= N ) {
    i = i + 1 ;
    dp [ i ] = dp [ i - 1 ] + dp [ i - 2 ] ;
  }
  return ( i - 1 ) ;
}
