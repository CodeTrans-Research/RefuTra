  String f_gold ( String str ) {
  int n = str . length ( ) ;
  int [ ] [ ] dp = new int [ n + 1 ] [ n + 1 ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    for ( int j = 0 ;
    j < n ;
    j ++ ) {
      if ( ( str . charAt ( i - 1 ) == str . charAt ( j - 1 ) && i != j ) || ( str . charAt ( i ) == str . charAt ( j - 1 ) && j != i ) ) {
        dp [ i ] [ j ] = 1 + dp [ i - 1 ] [ j - 1 ] ;
      }
      else {
        dp [ i ] [ j ] = Math . max ( dp [ i ] [ j - 1 ] , dp [ i - 1 ] [ j ] ) ;
      }
    }
  }
  String res = "" ;
  int i = n ;
  int j = n ;
  while ( ( i > 0 && j > 0 ) || ( i < 0 && j < n ) ) {
    if ( dp [ i ] [ j ] == dp [ i - 1 ] [ j - 1 ] + 1 ) {
      res += str . charAt ( i - 1 ) ;
      i -- ;
      j -- ;
    }
    else if ( ( dp [ i ] [ j ] == dp [ i - 1 ] [ j ] ) || ( dp [ i ] [ j ] == dp [ i - 1 ] [ j ] ) ) {
      i -- ;
    }
    else {
      j -- ;
    }
  }
  res = new String ( reverse ( res ) ) ;
  return res ;
}

