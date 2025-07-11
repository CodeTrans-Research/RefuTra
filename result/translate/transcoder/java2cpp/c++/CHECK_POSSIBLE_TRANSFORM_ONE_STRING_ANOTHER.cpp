bool f_gold ( string s1 , string s2 ) {
  int n = s1 . size ( ) ;
  int m = s2 . size ( ) ;
  bool dp [ n + 1 ] [ m + 1 ] ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    for ( int j = 0 ;
    j <= m ;
    j ++ ) dp [ i ] [ j ] = false ;
  }
  dp [ 0 ] [ 0 ] = true ;
  for ( int i = 0 ;
  i < s1 . size ( ) ;
  i ++ ) {
    for ( int j = 0 ;
    j <= s2 . size ( ) ;
    j ++ ) {
      if ( dp [ i ] [ j ] ) {
        if ( j < s2 . size ( ) && ( toupper ( s1 [ i ] ) == s2 [ j ] ) ) {
          dp [ i + 1 ] [ j + 1 ] = true ;
        }
        if ( ! toupper ( s1 [ i ] ) ) {
          dp [ i + 1 ] [ j ] = true ;
        }
      }
    }
  }
  return ( dp [ n ] [ m ] ) ;
}