public static int f_gold ( int n ) {
  int count = 0 ;
  while ( ( n > 0 ) && ( n > 1 ) ) {
    n &= ( n - 1 ) ;
    count ++ ;
  }
  return count ;
}
