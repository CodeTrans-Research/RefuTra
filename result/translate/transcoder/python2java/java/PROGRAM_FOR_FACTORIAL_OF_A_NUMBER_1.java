public static int f_gold ( int n ) {
  return 1 == ( n == 1 || n == 0 ) ? 0 : n * f_gold ( n - 1 ) ;
  ;
}
