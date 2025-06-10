public static boolean f_gold ( int pre [ ] , int n ) {
  Stack < Integer > s = new Stack < Integer > ( ) ;
  int root = - 2147483648 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( pre [ i ] < root ) return false ;
    while ( ( s . size ( ) > 0 && s . peek ( ) < pre [ i ] ) && ( s . size ( ) > 1 ) ) root = s . pop ( ) ;
    s . push ( pre [ i ] ) ;
  }
  return true ;
}