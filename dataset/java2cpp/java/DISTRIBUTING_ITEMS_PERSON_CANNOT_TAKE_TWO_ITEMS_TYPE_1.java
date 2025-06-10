boolean f_gold ( int arr [ ] , int n , int k ) {
  HashMap < Integer , Integer > hash = new HashMap < > ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( ! hash . containsKey ( arr [ i ] ) ) hash . put ( arr [ i ] , 0 ) ;
    hash . put ( arr [ i ] , hash . get ( arr [ i ] ) + 1 ) ;
  }
  for ( Map . Entry x : hash . entrySet ( ) ) if ( ( int ) x . getValue ( ) > 2 * k ) return false ;
  return true ;
}