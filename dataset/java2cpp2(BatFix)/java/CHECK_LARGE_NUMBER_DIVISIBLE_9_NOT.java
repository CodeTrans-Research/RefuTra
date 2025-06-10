boolean f_gold ( String str ) {
  int n = str . length ( );
  int digitSum = 0;
  for ( int i = 0;
  i < n;
  i ++ ) digitSum += ( str . charAt ( i ) - '0' );
  return ( digitSum % 9 == 0 );
}