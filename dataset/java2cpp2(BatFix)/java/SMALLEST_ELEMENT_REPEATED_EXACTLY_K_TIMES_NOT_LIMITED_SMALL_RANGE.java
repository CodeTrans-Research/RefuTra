int f_gold ( int a [ ], int n, int k ) {
  HashMap < Integer, Integer > m = new HashMap < Integer, Integer > ( );
  for ( int i = 0;
  i < n;
  i ++ ) if ( m . containsKey ( a [ i ] ) ) m . put ( a [ i ], m . get ( a [ i ] ) + 1 );
  else m . put ( a [ i ], 1 );
  int res = Integer . MAX_VALUE;
  Set < Integer > s = m . keySet ( );
  for ( int temp : s ) if ( m . get ( temp ) == k ) res = Math . min ( res, temp );
  return ( res != Integer . MAX_VALUE ) ? res : - 1;
}