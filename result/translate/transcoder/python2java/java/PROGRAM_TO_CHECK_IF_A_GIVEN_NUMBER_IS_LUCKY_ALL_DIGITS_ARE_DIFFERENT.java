public static boolean f_gold ( int n ) {
  int [ ] ar = new int [ 10 ] ;
  ar [ 0 ] = 0 ;
  while ( ( n > 0 ) && ( ar [ 0 ] == 0 ) ) {
    int digit = Math . floor ( n % 10 ) ;
    if ( ( ar [ digit ] == 0 ) || ( ar [ digit ] == 1 ) ) {
      return false ;
    }
    ar [ digit ] = 1 ;
    n = ( int ) ( n / 10 ) ;
  }
  return true ;
}