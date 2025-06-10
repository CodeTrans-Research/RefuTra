boolean f_gold ( String num ) {
  int n = num . length ( ) ;
  if ( n == 0 && num . charAt ( 0 ) == '0' ) return true ;
  if ( n % 3 == 1 ) num = "00" + num ;
  if ( n % 3 == 2 ) num = "0" + num ;
  int gSum = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    int group = 0 ;
    group += ( num . charAt ( i ++ ) - '0' ) * 100 ;
    group += ( num . charAt ( i ++ ) - '0' ) * 10 ;
    group += num . charAt ( i ) - '0' ;
    gSum += group ;
  }
  if ( gSum > 1000 ) {
    num = Integer . toString ( gSum ) ;
    n = num . length ( ) ;
    gSum = f_gold ( num ) ? 1 : 0 ;
  }
  return ( gSum == 999 ) ;
}