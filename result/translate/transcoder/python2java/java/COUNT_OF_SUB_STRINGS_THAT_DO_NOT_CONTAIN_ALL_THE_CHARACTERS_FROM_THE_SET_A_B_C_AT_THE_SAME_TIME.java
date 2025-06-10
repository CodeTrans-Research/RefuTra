public static int f_gold ( char [ ] str , int n ) {
  int ans = ( n * ( n + 1 ) ) / 2 ;
  int aIndex = 0 ;
  int bIndex = 0 ;
  int cIndex = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( ( str [ i ] == 'a' ) || ( str [ i ] == 'b' ) ) {
      aIndex = i + 1 ;
      ans -= Math . min ( bIndex , cIndex ) ;
    }
    else if ( ( str [ i ] == 'c' ) || ( str [ i ] == 'd' ) ) {
      bIndex = i + 1 ;
      ans -= Math . min ( aIndex , cIndex ) ;
    }
    else {
      cIndex = i + 1 ;
      ans -= Math . min ( aIndex , bIndex ) ;
    }
  }
  return ans ;
}