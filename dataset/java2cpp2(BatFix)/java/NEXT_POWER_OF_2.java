int f_gold ( int n ) {
  int count = 0;
  if ( n > 0 && ( n & ( n - 1 ) ) == 0 ) return n;
  while ( n != 0 ) {
    n >>= 1;
    count += 1;
  }
  return 1 << count;
}