public static int f_gold ( int [ ] arr , int n ) {
  int [ ] freq = new int [ n ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    freq [ arr [ i ] ] ++ ;
  }
  int ans = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    for ( int j = 0 ;
    j < n ;
    j ++ ) {
      if ( freq [ arr [ i ] ] > freq [ arr [ j ] ] && arr [ i ] > arr [ j ] ) {
        ans = Math . max ( ans , freq [ arr [ i ] ] - freq [ arr [ j ] ] ) ;
      }
      else if ( freq [ arr [ i ] ] < freq [ arr [ j ] ] && arr [ i ] < arr [ j ] ) {
        ans = Math . max ( ans , freq [ arr [ j ] ] - freq [ arr [ i ] ] ) ;
      }
    }
  }
  return ans ;
}