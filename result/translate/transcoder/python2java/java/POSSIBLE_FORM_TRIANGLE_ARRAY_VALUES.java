public static boolean fGoldenArray ( int [ ] arr , int N ) {
  int [ ] array = new int [ N ] ;
  if ( N < 3 ) return false ;
  Arrays . sort ( array ) ;
  for ( int i = 0 ;
  i < N - 2 ;
  i ++ ) {
    if ( array [ i ] + array [ i + 1 ] > array [ i + 2 ] ) return true ;
  }
  return false ;
}