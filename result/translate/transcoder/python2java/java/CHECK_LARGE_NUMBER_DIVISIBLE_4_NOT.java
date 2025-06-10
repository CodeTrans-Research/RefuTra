public static boolean f_gold ( String str ) {
  int n = str . length ( ) ;
  if ( ( n == 0 ) || ( n == 1 ) ) return false ;
  if ( ( n == 2 ) || ( n == 3 ) ) return ( ( str . charAt ( 0 ) - '0' ) % 4 == 0 ) ;
  int last = ( int ) ( str . charAt ( n - 1 ) ) ;
  int secondLast = ( int ) ( str . charAt ( n - 2 ) ) ;
  return ( ( secondLast * 10 + last ) % 4 == 0 ) ;
}