int f_gold ( String str, int n ) {
  char last = ' ';
  int res = 0;
  for ( int i = 0;
  i < n;
  i ++ ) {
    if ( last != str . charAt ( i ) ) res ++;
    last = str . charAt ( i );
  }
  return res / 2;
}