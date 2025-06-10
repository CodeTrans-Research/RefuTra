int f_gold ( String N ) {
  int len = N . length ( );
  int l = ( len ) / 2;
  int count = 0;
  for ( int i = 1;
  i <= l;
  i ++ ) {
    String s = N . substring ( 0, i );
    int l1 = s . length ( );
    String t = N . substring ( i, l1 + i );
    if ( s . charAt ( 0 ) == '0' || t . charAt ( 0 ) == '0' ) continue;
    if ( s . compareTo ( t ) == 0 ) count ++;
  }
  return count;
}