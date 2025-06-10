boolean f_gold ( double m [ ] [ ] ) {
  for ( int i = 0 ;
  i < m . length ;
  i ++ ) {
    double sum = 0 ;
    for ( int j = 0 ;
    j < m [ i ] . length ;
    j ++ ) sum = sum + m [ i ] [ j ] ;
    if ( sum != 1 ) return false ;
  }
  return true ;
}