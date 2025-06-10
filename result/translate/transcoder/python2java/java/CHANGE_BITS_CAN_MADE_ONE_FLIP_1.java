public static boolean f_gold ( String str ) {
  int sum = 0 ;
  int n = str . length ( ) ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) sum += ( char ) str . charAt ( i ) - ( char ) '0' ;
  return ( sum == n - 1 || sum == 1 ) ;
}