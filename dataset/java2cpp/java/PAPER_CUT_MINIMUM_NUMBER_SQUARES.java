int f_gold ( int a , int b ) {
  int result = 0 , rem = 0 ;
  if ( a < b ) swap ( a , b ) ;
  while ( b > 0 ) {
    result += a / b ;
    rem = a % b ;
    a = b ;
    b = rem ;
  }
  return result ;
}