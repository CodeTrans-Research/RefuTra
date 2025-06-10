public static int f_gold ( int start , int end , int [ ] arr ) {
  Map < Integer , Integer > frequency = new HashMap < Integer , Integer > ( ) ;
  for ( int i = start ;
  i <= end ;
  i ++ ) {
    if ( arr [ i ] < frequency . keySet ( ) . size ( ) ) {
      frequency . put ( arr [ i ] , 1 ) ;
    }
    else {
      frequency . put ( arr [ i ] , 1 ) ;
    }
  }
  int count = 0 ;
  for ( int x : frequency . keySet ( ) ) {
    if ( x == frequency . get ( x ) ) {
      count ++ ;
    }
  }
  return count ;
}
