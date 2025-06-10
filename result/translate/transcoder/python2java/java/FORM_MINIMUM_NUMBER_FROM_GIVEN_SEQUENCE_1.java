public static String f_gold ( String seq ) {
  int n = seq . length ( ) ;
  if ( ( n >= 9 ) && ( seq . charAt ( n ) == 'I' ) ) {
    return "-1" ;
  }
  StringBuilder sb = new StringBuilder ( n + 1 ) ;
  int count = 1 ;
  for ( int i = 0 ;
  i < n + 1 ;
  i ++ ) {
    if ( ( i == n || seq . charAt ( i ) == 'I' ) && ( seq . charAt ( i + 1 ) == 'I' ) ) {
      for ( int j = i - 1 ;
      j >= 0 ;
      j -- ) {
        sb . append ( ( char ) ( '0' + count ) ) ;
        count ++ ;
        if ( ( j >= 0 && seq . charAt ( j ) == 'I' ) && ( seq . charAt ( j + 1 ) == 'I' ) ) {
          break ;
        }
      }
    }
  }
  return sb . toString ( ) ;
}
