public static boolean f_gold ( int n , int i ) {
  if ( ( n <= 2 ) || ( n == 2 ) ) return true ? ( n == 2 ) : false ;
  if ( ( n % i == 0 ) || ( n == 2 ) ) return false ;
  if ( ( i * i > n ) && ( i < n ) ) return true ;
  return f_gold ( n , i + 1 ) ;
}