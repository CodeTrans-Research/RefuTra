String f_gold ( String s ) {
  int l = s . length ( );
  String s1 = "";
  boolean isEven = ( l % 2 == 0 ) ? true : false;
  for ( int i = 0;
  i < l;
  i += 2 ) {
    if ( isEven ) {
      s1 = s . charAt ( i ) + s1;
      s1 += s . charAt ( i + 1 );
    }
    else {
      if ( l - i > 1 ) {
        s1 += s . charAt ( i );
        s1 = s . charAt ( i + 1 ) + s1;
      }
      else {
        s1 += s . charAt ( i );
      }
    }
  }
  return s1;
}