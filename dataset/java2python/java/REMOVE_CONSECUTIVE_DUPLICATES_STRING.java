void f_gold ( char [ ] S ) {
  int n = S . length ;
  if ( n < 2 ) {
    return ;
  }
  int j = 0 ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    if ( S [ j ] != S [ i ] ) {
      j ++ ;
      S [ j ] = S [ i ] ;
    }
  }
  System . out . println ( Arrays . copyOfRange ( S , 0 , j + 1 ) ) ;
}