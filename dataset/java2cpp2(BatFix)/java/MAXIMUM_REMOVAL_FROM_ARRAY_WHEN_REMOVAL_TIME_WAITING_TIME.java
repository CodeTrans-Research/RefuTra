int f_gold ( int arr [ ], int n ) {
  int count = 0;
  int cummulative_sum = 0;
  Arrays . sort ( arr );
  for ( int i = 0;
  i < n;
  i ++ ) {
    if ( arr [ i ] >= cummulative_sum ) {
      count ++;
      cummulative_sum += arr [ i ];
    }
  }
  return count;
}