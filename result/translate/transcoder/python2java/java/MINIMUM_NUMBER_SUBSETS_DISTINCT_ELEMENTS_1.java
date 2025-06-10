public static int f_gold ( int [ ] arr , int n ) {
  int maxv = max ( arr ) ;
  int minv = min ( arr ) ;
  int [ ] mp = new int [ minv + maxv + 1 ] ;
  for ( int i = minv ;
  i <= maxv ;
  i ++ ) {
    mp [ arr [ i ] ] ++ ;
  }
  int res = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    res = max ( res , mp [ i ] ) ;
  }
  return res ;
}