private  int f_gold ( int [ ] arr, int n ) {
  int jumps [ ] = new int [ n ];
  int i, j;
  if ( n == 0 || arr [ 0 ] == 0 ) return Integer . MAX_VALUE;
  jumps [ 0 ] = 0;
  for ( i = 1;
  i < n;
  i ++ ) {
    jumps [ i ] = Integer . MAX_VALUE;
    for ( j = 0;
    j < i;
    j ++ ) {
      if ( i <= j + arr [ j ] && jumps [ j ] != Integer . MAX_VALUE ) {
        jumps [ i ] = Math . min ( jumps [ i ], jumps [ j ] + 1 );
        break;
      }
    }
  }
  return jumps [ n - 1 ];
}