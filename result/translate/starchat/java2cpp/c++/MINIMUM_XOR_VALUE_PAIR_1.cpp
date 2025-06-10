int f_gold ( int arr [ ], int n ) {
  arr = new int [n];
  std :: copy ( arr, arr + n, std :: begin ( arr ) ) ;
  std :: sort ( std :: begin ( arr ), std :: end ( arr ) ) ;
  int minXor = INT_MAX ;
  int val = 0 ;
  for ( int i = 0 ;
  i < n - 1 ;
  i ++ ) {
    val = arr [ i ] ^ arr [ i + 1 ] ;
    minXor = std :: min ( minXor, val ) ;
  }
  return minXor ;
}