int f_gold ( int arr [ ] , int n ) {
  Map < Integer , Integer > freq = new HashMap < > ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) freq . put ( arr [ i ] , freq . get ( arr [ i ] ) == null ? 1 : freq . get ( arr [ i ] ) + 1 ) ;
  int ans = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    for ( int j = 0 ;
    j < n ;
    j ++ ) {
      if ( freq . get ( arr [ i ] ) > freq . get ( arr [ j ] ) && arr [ i ] > arr [ j ] ) ans = Math . max ( ans , freq . get ( arr [ i ] ) - freq . get ( arr [ j ] ) ) ;
      else if ( freq . get ( arr [ i ] ) < freq . get ( arr [ j ] ) && arr [ i ] < arr [ j ] ) ans = Math . max ( ans , freq . get ( arr [ j ] ) - freq . get ( arr [ i ] ) ) ;
    }
  }
  return ans ;
}