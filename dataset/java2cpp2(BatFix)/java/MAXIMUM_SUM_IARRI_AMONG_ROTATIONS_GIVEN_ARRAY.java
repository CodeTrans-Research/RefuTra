int f_gold ( int arr [ ], int n ) {
  int res = Integer . MIN_VALUE;
  for ( int i = 0;
  i < n;
  i ++ ) {
    int curr_sum = 0;
    for ( int j = 0;
    j < n;
    j ++ ) {
      int index = ( i + j ) % n;
      curr_sum += j * arr [ index ];
    }
    res = Math . max ( res, curr_sum );
  }
  return res;
}