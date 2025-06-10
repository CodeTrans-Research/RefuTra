String f_gold ( String seq ) {
  int n = seq . length ( ) ;
  if ( n >= 9 ) return "-1" ;
  char result [ ] = new char [ n + 1 ] ;
  int count = 1 ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    if ( i == n || seq . charAt ( i ) == 'I' ) {
      for ( int j = i - 1 ;
      j >= - 1 ;
      j -- ) {
        result [ j + 1 ] = ( char ) ( ( int ) '0' + count ++ ) ;
        if ( j >= 0 && seq . charAt ( j ) == 'I' ) break ;
      }
    }
  }
  return new String ( result ) ;
}