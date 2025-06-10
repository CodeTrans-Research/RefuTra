long f_gold ( long a , long b , long mod ) {
  long res = 0 ;
  a = a % mod ;
  while ( b > 0 ) {
    if ( b % 2 == 1 ) {
      res = ( res + a ) % mod ;
    }
    a = ( a * 2 ) % mod ;
    b /= 2 ;
  }
  return res % mod ;
}