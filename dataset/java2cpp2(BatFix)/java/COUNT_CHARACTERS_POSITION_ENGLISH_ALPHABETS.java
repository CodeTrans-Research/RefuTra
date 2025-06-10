int f_gold ( String str ) {
  int result = 0;
  for ( int i = 0;
  i < str . length ( );
  i ++ ) {
    if ( i == ( str . charAt ( i ) - 'a' ) || i == ( str . charAt ( i ) - 'A' ) ) {
      result ++;
    }
  }
  return result;
}