static int f_gold ( int n ) {
  int [ ] f = new int [ n + 1 ] ;
  for ( int i = 3 ;
  i <= n ;
  i ++ ) {
    int r = f [ f [ i - 1 ] ] + f [ i - f [ i - 1 ] ] ;
    f [ i ] = r ;
  }
  return f [ n ] ;
}