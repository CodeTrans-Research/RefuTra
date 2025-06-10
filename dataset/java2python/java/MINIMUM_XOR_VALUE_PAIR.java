int f_gold ( int arr [ ] , int n ) {
  int min_xor = Integer . MAX_VALUE ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) for ( int j = i + 1 ;
  j < n ;
  j ++ ) min_xor = Math . min ( min_xor , arr [ i ] ^ arr [ j ] ) ;
  return min_xor ;
}