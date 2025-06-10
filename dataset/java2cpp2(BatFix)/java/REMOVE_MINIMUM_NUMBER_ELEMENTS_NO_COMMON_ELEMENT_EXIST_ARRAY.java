int f_gold ( int a [ ], int b [ ], int n, int m ) {
  HashMap < Integer, Integer > countA = new HashMap < Integer, Integer > ( );
  HashMap < Integer, Integer > countB = new HashMap < Integer, Integer > ( );
  for ( int i = 0;
  i < n;
  i ++ ) {
    if ( countA . containsKey ( a [ i ] ) ) countA . put ( a [ i ], countA . get ( a [ i ] ) + 1 );
    else countA . put ( a [ i ], 1 );
  }
  for ( int i = 0;
  i < m;
  i ++ ) {
    if ( countB . containsKey ( b [ i ] ) ) countB . put ( b [ i ], countB . get ( b [ i ] ) + 1 );
    else countB . put ( b [ i ], 1 );
  }
  int res = 0;
  Set < Integer > s = countA . keySet ( );
  for ( int x : s ) if ( countB . containsKey ( x ) ) res += Math . min ( countB . get ( x ), countA . get ( x ) );
  return res;
}