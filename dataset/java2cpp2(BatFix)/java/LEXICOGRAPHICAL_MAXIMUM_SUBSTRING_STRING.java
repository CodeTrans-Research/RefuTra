String f_gold ( String str ) {
  String mx = "";
  for ( int i = 0;
  i < str . length ( );
  ++ i ) {
    if ( mx . compareTo ( str . substring ( i ) ) <= 0 ) {
      mx = str . substring ( i );
    }
  }
  return mx;
}