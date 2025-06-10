boolean f_gold ( int a [ ] , int n ) {
  HashMap < Integer , Integer > mp = new HashMap < Integer , Integer > ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) if ( mp . containsKey ( a [ i ] ) ) mp . put ( a [ i ] , mp . get ( a [ i ] ) + 1 ) ;
  else mp . put ( a [ i ] , 1 ) ;
  for ( Map . Entry < Integer , Integer > x : mp . entrySet ( ) ) if ( x . getValue ( ) >= n / 2 ) return true ;
  return false ;
}