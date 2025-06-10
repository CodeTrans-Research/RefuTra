long f_gold ( long n ) {
  if ( n == 0 || n == 1 ) return 1;
  return n * f_gold ( n - 2 );
}