public static int f_gold ( int [ ] arr , int n ) {
  TreeMap < Integer , Integer > um = new TreeMap < Integer , Integer > ( ) ;
  int longLen = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    int len1 = 0 ;
    if ( ( arr [ i - 1 ] < 0 ) && len1 < um . get ( arr [ i ] - 1 ) ) {
      len1 = um . get ( arr [ i ] - 1 ) ;
    }
    if ( ( arr [ i ] + 1 < 0 ) && len1 < um . get ( arr [ i ] + 1 ) ) {
      len1 = um . get ( arr [ i ] + 1 ) ;
    }
    um . put ( arr [ i ] , len1 + 1 ) ;
    if ( longLen < um . get ( arr [ i ] ) ) {
      longLen = um . get ( arr [ i ] ) ;
    }
  }
  return longLen ;
}