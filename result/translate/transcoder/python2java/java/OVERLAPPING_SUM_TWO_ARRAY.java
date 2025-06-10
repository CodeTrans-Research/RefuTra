public static int f_gold ( int [ ] A , int [ ] B , int n ) {
  TreeMap < Integer , Integer > Hash = new TreeMap < Integer , Integer > ( ) ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    Hash . put ( A [ i ] , 0 ) ;
    Hash . put ( B [ i ] , 1 ) ;
  }
  int Sum = 0 ;
  for ( int x : Hash . keySet ( ) ) {
    if ( Hash . get ( x ) == 1 ) Sum += x ;
  }
  return Sum ;
}