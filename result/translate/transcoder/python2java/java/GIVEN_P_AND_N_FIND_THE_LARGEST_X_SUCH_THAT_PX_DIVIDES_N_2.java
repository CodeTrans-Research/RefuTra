static int f_gold ( int n , int p ) {
  int x = 0 ;
  while ( n > 0 ) {
    n /= p ;
    x += n ;
  }
  return x ;
}