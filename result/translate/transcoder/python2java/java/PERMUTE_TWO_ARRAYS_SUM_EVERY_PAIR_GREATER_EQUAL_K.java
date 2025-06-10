public static boolean f_gold ( int [ ] a , int [ ] b , int n , int k ) {
  int [ ] a = new int [ n ] ;
  int [ ] b = new int [ n ] ;
  Arrays . sort ( a ) ;
  Arrays . sort ( b ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( ( a [ i ] + b [ i ] ) < k ) return false ;
  }
  return true ;
}