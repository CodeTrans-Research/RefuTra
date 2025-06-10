int f_gold ( String str, int n ) {
  int len = str . length ( );
  int dp [ ] [ ] = new int [ len ] [ n ];
  dp [ 0 ] [ ( str . charAt ( 0 ) - '0' ) % n ] ++;
  for ( int i = 1;
  i < len;
  i ++ ) {
    dp [ i ] [ ( str . charAt ( i ) - '0' ) % n ] ++;
    for ( int j = 0;
    j < n;
    j ++ ) {
      dp [ i ] [ j ] += dp [ i - 1 ] [ j ];
      dp [ i ] [ ( j * 10 + ( str . charAt ( i ) - '0' ) ) % n ] += dp [ i - 1 ] [ j ];
    }
  }
  return dp [ len - 1 ] [ 0 ];
}