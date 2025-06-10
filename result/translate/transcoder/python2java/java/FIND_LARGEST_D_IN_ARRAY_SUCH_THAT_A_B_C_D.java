public static int f_gold ( int [ ] S , int n ) {
  boolean found = false ;
  int [ ] S = new int [ n ] ;
  Arrays . sort ( S ) ;
  for ( int i = n - 1 ;
  i >= 0 ;
  i -- ) {
    for ( int j = 0 ;
    j <= n ;
    j ++ ) {
      if ( ( i == j ) && ( i < n ) ) continue ;
      for ( int k = j + 1 ;
      k <= n ;
      k ++ ) {
        if ( ( i == k ) && ( i < n ) ) continue ;
        for ( int l = k + 1 ;
        l <= n ;
        l ++ ) {
          if ( ( i == l ) && ( i < n ) ) continue ;
          if ( ( S [ i ] == S [ j ] + S [ k ] + S [ l ] ) || ( S [ i ] == S [ j ] + S [ k ] + S [ l ] ) ) {
            found = true ;
            return S [ i ] ;
          }
        }
      }
    }
  }
  if ( ( found == false ) && ( n > 0 ) ) return - 1 ;
  return 0 ;
}