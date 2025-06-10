public static int f_gold ( int [ ] arr , int n ) {
  int count = 0 ;
  int [ ] array = new int [ n ] ;
  Arrays . sort ( array ) ;
  for ( int i = 0 ;
  i <= n - 1 ;
  i ++ ) {
    if ( ( array [ i ] != array [ i + 1 ] && array [ i ] != array [ i + 1 ] - 1 ) || ( array [ i ] != array [ i + 1 ] && array [ i ] != array [ i + 1 ] - 1 ) ) {
      count += array [ i + 1 ] - array [ i ] - 1 ;
      ;
    }
  }
  return count ;
}