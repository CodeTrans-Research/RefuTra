public static int f_gold ( int x ) {
  int next = 0 ;
  if ( ( x > 0 ) && ( x < ( x + 1 ) ) ) {
    int rightOne = x & - ( x ) ;
    int nextHigherOneBit = x + Integer . numberOfTrailingZeros ( rightOne ) ;
    int rightOnesPattern = x ^ Integer . numberOfTrailingZeros ( nextHigherOneBit ) ;
    rightOnesPattern = ( Integer . numberOfTrailingZeros ( rightOnesPattern ) / Integer . numberOfLeadingZeros ( rightOne ) ) ;
    rightOnesPattern = Integer . numberOfTrailingZeros ( rightOnesPattern ) >> 2 ;
    next = nextHigherOneBit | rightOnesPattern ;
  }
  return next ;
}