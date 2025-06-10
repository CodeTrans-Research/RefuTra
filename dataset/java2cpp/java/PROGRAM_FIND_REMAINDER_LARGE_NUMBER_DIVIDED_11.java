int f_gold ( String str ) {
  int len = str . length ( ) ;
  int num , rem = 0 ;
  for ( int i = 0 ;
  i < len ;
  i ++ ) {
    num = rem * 10 + ( str . charAt ( i ) - '0' ) ;
    rem = num % 11 ;
  }
  return rem ;
}