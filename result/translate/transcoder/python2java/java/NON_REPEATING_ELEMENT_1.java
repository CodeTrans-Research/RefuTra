public static int f_gold ( int [ ] arr , int n ) {
  TreeMap < Integer , Integer > mp = new TreeMap < Integer , Integer > ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) mp . put ( arr [ i ] , 0 ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) if ( mp . get ( arr [ i ] ) == 1 ) return arr [ i ] ;
  return - 1 ;
}