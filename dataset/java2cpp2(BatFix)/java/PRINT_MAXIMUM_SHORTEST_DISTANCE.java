int f_gold ( int a [ ], int n, int k ) {
  HashMap < Integer, Integer > b = new HashMap < Integer, Integer > ( );
  for ( int i = 0;
  i < n;
  i ++ ) {
    int x = a [ i ];
    int d = Math . min ( 1 + i, n - i );
    if ( ! b . containsKey ( x ) ) b . put ( x, d );
    else {
      b . put ( x, Math . min ( d, b . get ( x ) ) );
    }
  }
  int ans = Integer . MAX_VALUE;
  for ( int i = 0;
  i < n;
  i ++ ) {
    int x = a [ i ];
    if ( x != k - x && b . containsKey ( k - x ) ) ans = Math . min ( Math . max ( b . get ( x ), b . get ( k - x ) ), ans );
  }
  return ans;
}