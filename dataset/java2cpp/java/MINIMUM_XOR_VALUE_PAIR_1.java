int f_gold ( int arr [ ] , int n ) {
  arr = Arrays.copyOfRange(arr, 0, n);
  Arrays . parallelSort ( arr ) ;
  int minXor = Integer . MAX_VALUE ;
  int val = 0 ;
  for ( int i = 0 ;
  i < n - 1 ;
  i ++ ) {
    val = arr [ i ] ^ arr [ i + 1 ] ;
    minXor = Math . min ( minXor , val ) ;
  }
  return minXor ;
}