int f_gold ( int a [ ], int n ) {
  int mn = Integer . MAX_VALUE;
  int sum = 0;
  for ( int i = 0;
  i < n;
  i ++ ) {
    mn = Math . min ( a [ i ], mn );
    sum += a [ i ];
  }
  return mn * ( sum - mn );
}