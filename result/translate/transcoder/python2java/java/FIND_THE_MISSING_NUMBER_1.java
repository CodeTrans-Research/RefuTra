static int f_gold ( int [ ] a , int n ) {
  int i , total = 0 ;
  for ( i = 2 ;
  i <= n ;
  i += 2 ) {
    total += i ;
    total -= a [ i - 2 ] ;
  }
  return total ;
}
