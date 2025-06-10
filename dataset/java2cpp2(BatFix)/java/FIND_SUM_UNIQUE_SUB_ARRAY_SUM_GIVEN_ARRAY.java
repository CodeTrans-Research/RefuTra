int f_gold ( int [ ] arr, int n ) {
  int res = 0;
  HashMap < Integer, Integer > m = new HashMap < Integer, Integer > ( );
  for ( int i = 0;
  i < n;
  i ++ ) {
    int sum = 0;
    for ( int j = i;
    j < n;
    j ++ ) {
      sum += arr [ j ];
      if ( m . containsKey ( sum ) ) {
        m . put ( sum, m . get ( sum ) + 1 );
      }
      else {
        m . put ( sum, 1 );
      }
    }
  }
  for ( Map . Entry < Integer, Integer > x : m . entrySet ( ) ) if ( x . getValue ( ) == 1 ) res += x . getKey ( );
  return res;
}