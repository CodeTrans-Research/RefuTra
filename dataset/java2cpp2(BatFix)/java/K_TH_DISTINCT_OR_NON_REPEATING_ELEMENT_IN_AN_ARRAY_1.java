int f_gold ( int arr [ ], int n, int k ) {
  Map < Integer, Integer > h = new HashMap < Integer, Integer > ( );
  for ( int i = 0;
  i < n;
  i ++ ) {
    if ( h . containsKey ( arr [ i ] ) ) h . put ( arr [ i ], h . get ( arr [ i ] ) + 1 );
    else h . put ( arr [ i ], 1 );
  }
  if ( h . size ( ) < k ) return - 1;
  int dist_count = 0;
  for ( int i = 0;
  i < n;
  i ++ ) {
    if ( h . get ( arr [ i ] ) == 1 ) dist_count ++;
    if ( dist_count == k ) return arr [ i ];
  }
  return - 1;
}