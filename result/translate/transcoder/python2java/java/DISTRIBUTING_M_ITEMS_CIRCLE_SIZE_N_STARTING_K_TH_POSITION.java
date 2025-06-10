public static int f_gold ( int n , int m , int k ) {
  if ( ( m <= n - k + 1 ) && ( m > n - k + 1 ) ) return m + k - 1 ;
  m = m - ( n - k + 1 ) ;
  if ( ( m % n == 0 ) || ( m % n == 1 ) ) return n ;
  else return m % n ;
}
