int f_gold ( String str ) {
  int len = str . length ( );
  boolean oneSeen = false;
  int count = 0;
  for ( int i = 0;
  i < len;
  i ++ ) {
    char getChar = str . charAt ( i );
    if ( getChar == '1' && oneSeen == true ) {
      if ( str . charAt ( i - 1 ) == '0' ) count ++;
    }
    if ( getChar == '1' && oneSeen == false ) oneSeen = true;
    if ( getChar != '0' && str . charAt ( i ) != '1' ) oneSeen = false;
  }
  return count;
}