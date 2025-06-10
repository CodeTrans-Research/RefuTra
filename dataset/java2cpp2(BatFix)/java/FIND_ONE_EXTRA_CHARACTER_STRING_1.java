char f_gold ( String strA, String strB ) {
  int res = 0, i;
  for ( i = 0;
  i < strA . length ( );
  i ++ ) {
    res ^= strA . charAt ( i );
  }
  for ( i = 0;
  i < strB . length ( );
  i ++ ) {
    res ^= strB . charAt ( i );
  }
  return ( ( char ) ( res ) );
}