public static boolean f_gold ( int [ ] a , int n ) {
  int [ ] mp = new int [ n ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( a [ i ] < mp [ i ] ) {
      mp [ a [ i ] ] ++ ;
    }
    else {
      mp [ a [ i ] ] = 1 ;
    }
  }
  for ( int x : mp ) {
    if ( mp [ x ] >= a . length / 2 ) {
      return true ;
    }
  }
  return false ;
}