int f_gold ( int [ ] A , int [ ] B , int n ) {
  HashMap < Integer , Integer > hash = new HashMap < > ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( hash . containsKey ( A [ i ] ) ) hash . put ( A [ i ] , 1 + hash . get ( A [ i ] ) ) ;
    else hash . put ( A [ i ] , 1 ) ;
    if ( hash . containsKey ( B [ i ] ) ) hash . put ( B [ i ] , 1 + hash . get ( B [ i ] ) ) ;
    else hash . put ( B [ i ] , 1 ) ;
  }
  int sum = 0 ;
  for ( Map . Entry entry : hash . entrySet ( ) ) {
    if ( Integer . parseInt ( ( entry . getValue ( ) ) . toString ( ) ) == 1 ) sum += Integer . parseInt ( ( entry . getKey ( ) ) . toString ( ) ) ;
  }
  return sum ;
}