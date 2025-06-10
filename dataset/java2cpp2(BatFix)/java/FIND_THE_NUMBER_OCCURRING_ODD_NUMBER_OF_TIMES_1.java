int f_gold ( int arr [ ], int n ) {
  HashMap < Integer, Integer > hmap = new HashMap < > ( );
  for ( int i = 0;
  i < n;
  i ++ ) {
    if ( hmap . containsKey ( arr [ i ] ) ) {
      int val = hmap . get ( arr [ i ] );
      hmap . put ( arr [ i ], val + 1 );
    }
    else hmap . put ( arr [ i ], 1 );
  }
  for ( Integer a : hmap . keySet ( ) ) {
    if ( hmap . get ( a ) % 2 != 0 ) return a;
  }
  return - 1;
}