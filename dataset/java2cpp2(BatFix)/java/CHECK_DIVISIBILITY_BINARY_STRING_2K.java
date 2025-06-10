boolean f_gold ( String str, int k ) {
  int n = str . length ( );
  int c = 0;
  for ( int i = 0;
  i < k;
  i ++ ) if ( str . charAt ( n - i - 1 ) == '0' ) c ++;
  return ( c == k );
}