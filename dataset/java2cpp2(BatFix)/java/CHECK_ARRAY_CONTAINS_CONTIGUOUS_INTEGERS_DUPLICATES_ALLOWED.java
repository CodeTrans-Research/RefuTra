boolean f_gold ( int arr [ ], int n ) {
  int max = Integer . MIN_VALUE;
  int min = Integer . MAX_VALUE;
  for ( int i = 0;
  i < n;
  i ++ ) {
    max = Math . max ( max, arr [ i ] );
    min = Math . min ( min, arr [ i ] );
  }
  int m = max - min + 1;
  if ( m > n ) return false;
  boolean visited [ ] = new boolean [ n ];
  for ( int i = 0;
  i < n;
  i ++ ) visited [ arr [ i ] - min ] = true;
  for ( int i = 0;
  i < m;
  i ++ ) if ( visited [ i ] == false ) return false;
  return true;
}