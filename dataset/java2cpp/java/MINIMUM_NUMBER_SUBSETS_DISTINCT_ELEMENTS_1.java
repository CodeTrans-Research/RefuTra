int f_gold ( int arr [ ] , int n ) {
  HashMap < Integer , Integer > mp = new HashMap < > ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) mp . put ( arr [ i ] , mp . get ( arr [ i ] ) == null ? 1 : mp . get ( arr [ i ] ) + 1 ) ;
  int res = 0 ;
  for ( Map . Entry < Integer , Integer > entry : mp . entrySet ( ) ) res = Math . max ( res , entry . getValue ( ) ) ;
  return res ;
}