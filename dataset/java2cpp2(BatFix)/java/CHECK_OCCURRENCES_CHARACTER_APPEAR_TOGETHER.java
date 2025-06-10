boolean f_gold ( String s, char c ) {
  boolean oneSeen = false;
  int i = 0, n = s . length ( );
  while ( i < n ) {
    if ( s . charAt ( i ) == c ) {
      if ( oneSeen == true ) return false;
      while ( i < n && s . charAt ( i ) == c ) i ++;
      oneSeen = true;
    }
    else i ++;
  }
  return true;
}