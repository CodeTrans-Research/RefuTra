int f_gold ( int x ) {
  int rightOne , nextHigherOneBit , rightOnesPattern , next = 0 ;
  if ( x > 0 ) {
    rightOne = x & - x ;
    nextHigherOneBit = x + rightOne ;
    rightOnesPattern = x ^ nextHigherOneBit ;
    rightOnesPattern = ( rightOnesPattern ) / rightOne ;
    rightOnesPattern >>= 2 ;
    next = nextHigherOneBit | rightOnesPattern ;
  }
  return next ;
}