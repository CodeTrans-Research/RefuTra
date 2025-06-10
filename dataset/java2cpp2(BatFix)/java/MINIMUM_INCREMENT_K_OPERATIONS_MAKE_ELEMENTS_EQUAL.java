int f_gold ( int arr [ ], int n, int k ) {
  Arrays . sort ( arr );
  int max = arr [ arr . length - 1 ];
  int res = 0;
  for ( int i = 0;
  i < n;
  i ++ ) {
    if ( ( max - arr [ i ] ) % k != 0 ) return - 1;
    else res += ( max - arr [ i ] ) / k;
  }
  return res;
}