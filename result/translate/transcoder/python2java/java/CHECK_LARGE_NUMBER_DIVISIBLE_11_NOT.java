public static boolean f_gold ( String str ) {
  int n = str . length ( ) ;
  int oddDigSum = 0 ;
  int evenDigSum = 0 ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    if ( ( i % 2 == 0 ) && ( i % 3 == 0 ) ) oddDigSum = oddDigSum + ( Character . digit ( str . charAt ( i ) , 16 ) - 48 ) ;
    else evenDigSum = evenDigSum + ( Character . digit ( str . charAt ( i ) , 16 ) - 48 ) ;
  }
  return ( ( oddDigSum - evenDigSum ) % 11 == 0 ) ;
}