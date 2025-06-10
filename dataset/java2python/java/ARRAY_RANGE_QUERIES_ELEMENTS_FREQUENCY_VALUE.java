int f_gold ( int start , int end , int arr [ ] ) {
  Map < Integer , Integer > mp = new HashMap < > ( ) ;
  for ( int i = start ;
  i <= end ;
  i ++ ) mp . put ( arr [ i ] , mp . get ( arr [ i ] ) == null ? 1 : mp . get ( arr [ i ] ) + 1 ) ;
  int count = 0 ;
  for ( Map . Entry < Integer , Integer > entry : mp . entrySet ( ) ) if ( entry . getKey ( ) == entry . getValue ( ) ) count ++ ;
  return count ;
}