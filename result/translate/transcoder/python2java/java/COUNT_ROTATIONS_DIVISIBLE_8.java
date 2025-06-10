public static int f_gold ( String n ) {
  int l = n . length ( ) ;
  int count = 0 ;
  if ( ( l == 1 ) && ( n . charAt ( 0 ) == '-' ) ) {
    int oneDigit = Integer . parseInt ( n . substring ( 0 , 1 ) ) ;
    if ( ( oneDigit % 8 == 0 ) || ( ( oneDigit % 8 == 1 ) && ( n . charAt ( 1 ) == '-' ) ) ) {
      return 1 ;
    }
    return 0 ;
  }
  if ( ( l == 2 ) && ( n . charAt ( 0 ) == '-' ) ) {
    int first = Integer . parseInt ( n . substring ( 0 , 1 ) ) * 10 + Integer . parseInt ( n . substring ( 1 , 2 ) ) ;
    int second = Integer . parseInt ( n . substring ( 1 , 2 ) ) * 10 + Integer . parseInt ( n . substring ( 0 , 2 ) ) ;
    if ( ( first % 8 == 0 ) || ( ( first % 8 == 1 ) && ( n . charAt ( 1 ) == '-' ) ) ) {
      count ++ ;
    }
    if ( ( second % 8 == 0 ) || ( ( second % 8 == 1 ) && ( n . charAt ( 1 ) == '-' ) ) ) {
      count ++ ;
    }
    return count ;
  }
  int threeDigit = 0 ;
  for ( int i = 0 ;
  i <= ( l - 2 ) ;
  i ++ ) {
    threeDigit = ( Integer . parseInt ( n . substring ( i , i + 1 ) ) * 100 + Integer . parseInt ( n . substring ( i + 1 , i + 2 ) ) * 10 + Integer . parseInt ( n . substring ( i + 2 ) ) ) ;
    if ( ( threeDigit % 8 == 0 ) || ( ( threeDigit % 8 == 1 ) && ( n . charAt ( i ) == '-' ) ) ) {
      count ++ ;
    }
  }
  threeDigit = ( Integer . parseInt ( n . substring ( l - 1 , l - 2 ) ) * 100 + Integer . parseInt ( n . substring ( l - 1 , l - 2 ) ) * 10 + Integer . parseInt ( n . substring ( 0 , l ) ) ) ;
  if ( ( threeDigit % 8 == 0 ) || ( ( threeDigit % 8 == 1 ) && ( n . charAt ( i ) == '-' ) ) ) {
    count ++ ;
  }
  return count ;
}