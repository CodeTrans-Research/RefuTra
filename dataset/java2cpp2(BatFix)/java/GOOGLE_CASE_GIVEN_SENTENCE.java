String f_gold ( String s ) {
  int n = s . length ( );
  String s1 = "";
  s1 = s1 + Character . toLowerCase ( s . charAt ( 0 ) );
  for ( int i = 1;
  i < n;
  i ++ ) {
    if ( s . charAt ( i ) == ' ' && i < n ) {
      s1 = s1 + " " + Character . toLowerCase ( s . charAt ( i + 1 ) );
      i ++;
    }
    else s1 = s1 + Character . toUpperCase ( s . charAt ( i ) );
  }
  return s1;
}