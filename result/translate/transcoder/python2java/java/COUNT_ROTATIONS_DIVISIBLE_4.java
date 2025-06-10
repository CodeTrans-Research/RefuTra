public static int f_gold ( String n ) {
  int l = n . length ( ) ;
  if ( ( l == 1 ) && ( n . charAt ( 0 ) == '-' ) ) {
    int oneDigit = ( int ) ( n . charAt ( 0 ) ) ;
    if ( ( oneDigit % 4 == 0 ) || ( oneDigit % 4 == 1 ) ) {
      return 1 ;
    }
    return 0 ;
  }
  int count = 0 ;
  for ( int i = 0 ;
  i <= l - 1 ;
  i ++ ) {
    int twoDigit = ( int ) ( n . charAt ( i ) ) * 10 + ( int ) ( n . charAt ( i + 1 ) ) ;
    if ( ( twoDigit % 4 == 0 ) || ( twoDigit % 4 == 1 ) ) {
      count = count + 1 ;
    }
  }
  int twoDigit = ( int ) ( n . charAt ( l - 1 ) ) * 10 + ( int ) ( n . charAt ( 0 ) ) ;
  if ( ( twoDigit % 4 == 0 ) || ( twoDigit % 4 == 1 ) ) {
    count = count + 1 ;
  }
  return count ;
}