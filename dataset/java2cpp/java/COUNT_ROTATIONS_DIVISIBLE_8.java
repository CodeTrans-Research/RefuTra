int f_gold ( String n ) {
  int len = n . length ( ) ;
  int count = 0 ;
  if ( len == 1 ) {
    int oneDigit = n . charAt ( 0 ) - '0' ;
    if ( oneDigit % 8 == 0 ) return 1 ;
    return 0 ;
  }
  if ( len == 2 ) {
    int first = ( n . charAt ( 0 ) - '0' ) * 10 + ( n . charAt ( 1 ) - '0' ) ;
    int second = ( n . charAt ( 1 ) - '0' ) * 10 + ( n . charAt ( 0 ) - '0' ) ;
    if ( first % 8 == 0 ) count ++ ;
    if ( second % 8 == 0 ) count ++ ;
    return count ;
  }
  int threeDigit ;
  for ( int i = 0 ;
  i < ( len - 2 ) ;
  i ++ ) {
    threeDigit = ( n . charAt ( i ) - '0' ) * 100 + ( n . charAt ( i + 1 ) - '0' ) * 10 + ( n . charAt ( i + 2 ) - '0' ) ;
    if ( threeDigit % 8 == 0 ) count ++ ;
  }
  threeDigit = ( n . charAt ( len - 1 ) - '0' ) * 100 + ( n . charAt ( 0 ) - '0' ) * 10 + ( n . charAt ( 1 ) - '0' ) ;
  if ( threeDigit % 8 == 0 ) count ++ ;
  threeDigit = ( n . charAt ( len - 2 ) - '0' ) * 100 + ( n . charAt ( len - 1 ) - '0' ) * 10 + ( n . charAt ( 0 ) - '0' ) ;
  if ( threeDigit % 8 == 0 ) count ++ ;
  return count ;
}