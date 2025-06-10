int f_gold ( String str ) {
  String tmp = str + str;
  int n = str . length ( );
  for ( int i = 1;
  i <= n;
  i ++ ) {
    String substring = tmp . substring ( i, str . length ( ) );
    if ( str == substring ) return i;
  }
  return n;
}