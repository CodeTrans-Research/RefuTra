public static int f_gold ( int n ) {
  int nCr = 1 ;
  int res = 1 ;
  for ( int r = 1 ;
  r <= n ;
  r ++ ) {
    nCr = ( int ) ( ( nCr * ( n + 1 - r ) ) / r ) ;
    res += nCr * nCr ;
  }
  return res ;
}