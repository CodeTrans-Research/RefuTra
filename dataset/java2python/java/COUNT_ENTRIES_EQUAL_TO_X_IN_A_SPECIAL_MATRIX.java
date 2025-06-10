int f_gold ( int n , int x ) {
  int f_gold = 0 ;
  for ( int i = 1 ;
  i <= n && i <= x ;
  i ++ ) {
    if ( x / i <= n && x % i == 0 ) f_gold ++ ;
  }
  return f_gold ;
}