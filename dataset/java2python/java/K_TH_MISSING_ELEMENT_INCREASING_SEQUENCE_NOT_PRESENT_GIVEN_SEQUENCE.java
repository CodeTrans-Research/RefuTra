int f_gold ( int a [ ] , int b [ ] , int k , int n1 , int n2 ) {
  LinkedHashSet < Integer > s = new LinkedHashSet < > ( ) ;
  for ( int i = 0 ;
  i < n2 ;
  i ++ ) s . add ( b [ i ] ) ;
  int missing = 0 ;
  for ( int i = 0 ;
  i < n1 ;
  i ++ ) {
    if ( ! s . contains ( a [ i ] ) ) missing ++ ;
    if ( missing == k ) return a [ i ] ;
  }
  return - 1 ;
}