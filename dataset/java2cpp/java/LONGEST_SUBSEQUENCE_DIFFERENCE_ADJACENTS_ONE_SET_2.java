int f_gold ( int [ ] arr , int n ) {
  HashMap < Integer , Integer > um = new HashMap < Integer , Integer > ( ) ;
  int longLen = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    int len = 0 ;
    if ( um . containsKey ( arr [ i ] - 1 ) && len < um . get ( arr [ i ] - 1 ) ) len = um . get ( arr [ i ] - 1 ) ;
    if ( um . containsKey ( arr [ i ] + 1 ) && len < um . get ( arr [ i ] + 1 ) ) len = um . get ( arr [ i ] + 1 ) ;
    um . put ( arr [ i ] , len + 1 ) ;
    if ( longLen < um . get ( arr [ i ] ) ) longLen = um . get ( arr [ i ] ) ;
  }
  return longLen ;
}