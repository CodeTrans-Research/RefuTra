int f_gold ( int a [ ], int n ) {
  Map < Integer, Integer > cnt = new HashMap < Integer, Integer > ( );
  int ans = 0, pre_sum = 0;
  for ( int i = 0;
  i < n;
  i ++ ) {
    ans += ( i * a [ i ] ) - pre_sum;
    pre_sum += a [ i ];
    if ( cnt . containsKey ( a [ i ] - 1 ) ) ans -= cnt . get ( a [ i ] - 1 );
    if ( cnt . containsKey ( a [ i ] + 1 ) ) ans += cnt . get ( a [ i ] + 1 );
    if ( cnt . containsKey ( a [ i ] ) ) {
      cnt . put ( a [ i ], cnt . get ( a [ i ] ) + 1 );
    }
    else {
      cnt . put ( a [ i ], 1 );
    }
  }
  return ans;
}