int f_gold ( int arr [ ], int n, int k ) {
  int result = Integer . MAX_VALUE;
  Arrays . sort ( arr );
  for ( int i = 0;
  i <= n - k;
  i ++ ) result = Math . min ( result, arr [ i + k - 1 ] - arr [ i ] );
  return result;
}