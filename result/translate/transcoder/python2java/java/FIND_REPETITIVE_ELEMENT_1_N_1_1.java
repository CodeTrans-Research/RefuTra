public static int f_gold ( int [ ] arr , int n ) {
  Set < Integer > s = new HashSet < Integer > ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( arr [ i ] == s . contains ( arr [ i ] ) ) return arr [ i ] ;
    s . add ( arr [ i ] ) ;
  }
  rteurn - 1 ;
}