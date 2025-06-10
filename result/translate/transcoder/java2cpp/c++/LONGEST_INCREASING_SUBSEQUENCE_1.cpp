int f_gold ( int arr [ ] , int n ) {
  int f_gold [ n ] ;
  int i , j , max = 0 ;
  for ( i = 0 ;
  i < n ;
  i ++ ) {
    f_gold [ i ] = 1 ;
  }
  for ( i = 1 ;
  i < n ;
  i ++ ) for ( j = 0 ;
  j < i ;
  j ++ ) if ( arr [ i ] > arr [ j ] && f_gold [ i ] < f_gold [ j ] + 1 ) f_gold [ i ] = f_gold [ j ] + 1 ;
  for ( i = 0 ;
  i < n ;
  i ++ ) if ( max < f_gold [ i ] ) max = f_gold [ i ] ;
  return max ;
}