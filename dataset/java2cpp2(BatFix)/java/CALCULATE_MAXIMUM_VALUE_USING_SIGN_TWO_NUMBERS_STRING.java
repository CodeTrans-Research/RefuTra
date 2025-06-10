int f_gold ( String str ) {
  int res = str . charAt ( 0 ) - '0';
  for ( int i = 1;
  i < str . length ( );
  i ++ ) {
    if ( str . charAt ( i ) == '0' || str . charAt ( i ) == '1' || res < 2 ) res += ( str . charAt ( i ) - '0' );
    else res *= ( str . charAt ( i ) - '0' );
  }
  return res;
}