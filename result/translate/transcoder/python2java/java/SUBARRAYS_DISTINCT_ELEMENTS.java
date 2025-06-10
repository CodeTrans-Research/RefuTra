public static int f_gold ( int [ ] arr , int n ) {
  ArrayList < Integer > s = new ArrayList < Integer > ( ) ;
  int j = 0 ;
  int ans = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    while ( ( j < n ) && ( arr [ j ] != null ) ) {
      s . add ( arr [ j ] ) ;
      j ++ ;
    }
    ans += ( ( j - i ) * ( j - i + 1 ) ) / 2 ;
    s . remove ( arr [ i ] ) ;
  }
  return ans ;
}
