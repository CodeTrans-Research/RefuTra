int f_gold ( int n, int a, int b ) {
  if ( n == 0 ) return a;
  if ( n == 1 ) return b;
  return f_gold ( n - 1, b, a + b );
}