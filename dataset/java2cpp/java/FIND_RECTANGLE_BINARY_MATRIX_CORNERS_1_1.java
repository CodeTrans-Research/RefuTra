boolean f_gold ( int matrix [ ] [ ] ) {
  int rows = matrix . length ;
  if ( rows == 0 ) return false ;
  int columns = matrix [ 0 ] . length ;
  HashMap < Integer , HashSet < Integer >> table = new HashMap < > ( ) ;
  for ( int i = 0 ;
  i < rows ;
  i ++ ) {
    for ( int j = 0 ;
    j < columns - 1 ;
    j ++ ) {
      for ( int k = j + 1 ;
      k < columns ;
      k ++ ) {
        if ( matrix [ i ] [ j ] == 1 && matrix [ i ] [ k ] == 1 ) {
          if ( table . containsKey ( j ) && table . get ( j ) . contains ( k ) ) {
            return true ;
          }
          if ( table . containsKey ( k ) && table . get ( k ) . contains ( j ) ) {
            return true ;
          }
          if ( ! table . containsKey ( j ) ) {
            HashSet < Integer > x = new HashSet < > ( ) ;
            x . add ( k ) ;
            table . put ( j , x ) ;
          }
          else {
            table . get ( j ) . add ( k ) ;
          }
          if ( ! table . containsKey ( k ) ) {
            HashSet < Integer > x = new HashSet < > ( ) ;
            x . add ( j ) ;
            table . put ( k , x ) ;
          }
          else {
            table . get ( k ) . add ( j ) ;
          }
        }
      }
    }
  }
  return false ;
}