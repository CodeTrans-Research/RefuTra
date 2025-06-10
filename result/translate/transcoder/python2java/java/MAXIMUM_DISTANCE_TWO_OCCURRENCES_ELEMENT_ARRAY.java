public static int f_gold ( int [ ] arr , int n ) {
  HashMap < Integer , Integer > mp = new HashMap < Integer , Integer > ( ) ;
  int maxDict = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( arr [ i ] != 0 ) {
      mp . put ( arr [ i ] , i ) ;
    }
    else {
      maxDict = Math . max ( maxDict , i - mp . get ( arr [ i ] ) ) ;
    }
  }
  return maxDict ;
}
