int f_gold ( int arr [ ], int n, int sum ) {
  HashMap < Integer, Integer > prevSum = new HashMap < > ( );
  int res = 0;
  int currsum = 0;
  for ( int i = 0;
  i < n;
  i ++ ) {
    currsum += arr [ i ];
    if ( currsum == sum ) res ++;
    if ( prevSum . containsKey ( currsum - sum ) ) res += prevSum . get ( currsum - sum );
    Integer count = prevSum . get ( currsum );
    if ( count == null ) prevSum . put ( currsum, 1 );
    else prevSum . put ( currsum, count + 1 );
  }
  return res;
}