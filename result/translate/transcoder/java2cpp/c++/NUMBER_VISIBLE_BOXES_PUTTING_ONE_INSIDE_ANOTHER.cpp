int f_gold ( int * arr , int n ) {
  queue < int > q ;
  arr = std :: copy ( arr , arr + n , queue < int > ( ) ) ;
  std :: sort ( arr , arr + n , queue < int > ( ) ) ;
  q . push ( arr [ 0 ] ) ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    int now = q . front ( ) ;
    if ( arr [ i ] >= 2 * now ) {
      q . pop ( ) ;
    }
    q . push ( arr [ i ] ) ;
  }
  return q . size ( ) ;
}