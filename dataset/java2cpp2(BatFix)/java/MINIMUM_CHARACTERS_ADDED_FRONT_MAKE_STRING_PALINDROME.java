boolean f_gold ( String s ) {
  int l = s . length ( );
  for ( int i = 0, j = l - 1;
  i <= j;
  i ++, j -- ) {
    if ( s . charAt ( i ) != s . charAt ( j ) ) {
      return false;
    }
  }
  return true;
}