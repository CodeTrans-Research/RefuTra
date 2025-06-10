boolean f_gold ( String str ) {
  int n = str . length ( );
  if ( ( str . charAt ( n - 1 ) - '0' ) % 2 != 0 ) return false;
  int digitSum = 0;
  for ( int i = 0;
  i < n;
  i ++ ) digitSum += ( str . charAt ( i ) - '0' );
  return ( digitSum % 3 == 0 );
}