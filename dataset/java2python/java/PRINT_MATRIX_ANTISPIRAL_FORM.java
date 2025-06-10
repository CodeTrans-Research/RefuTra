void f_gold ( int m , int n , int a [ ] [ ] ) {
  int i , k = 0 , l = 0 ;
  Stack < Integer > stk = new Stack < Integer > ( ) ;
  while ( k <= m && l <= n ) {
    for ( i = l ;
    i <= n ;
    ++ i ) stk . push ( a [ k ] [ i ] ) ;
    k ++ ;
    for ( i = k ;
    i <= m ;
    ++ i ) stk . push ( a [ i ] [ n ] ) ;
    n -- ;
    if ( k <= m ) {
      for ( i = n ;
      i >= l ;
      -- i ) stk . push ( a [ m ] [ i ] ) ;
      m -- ;
    }
    if ( l <= n ) {
      for ( i = m ;
      i >= k ;
      -- i ) stk . push ( a [ i ] [ l ] ) ;
      l ++ ;
    }
  }
  while ( ! stk . empty ( ) ) {
    System . out . print ( stk . peek ( ) + " " ) ;
    stk . pop ( ) ;
  }
}