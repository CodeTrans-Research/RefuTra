int f_gold ( int num, int divisor ) {
  if ( divisor == 0 ) {
    System . out . println ( "Error: divisor " + "can't be zero \n" );
    return - 1;
  }
  if ( divisor < 0 ) divisor = - divisor;
  if ( num < 0 ) num = - num;
  int i = 1;
  int product = 0;
  while ( product <= num ) {
    product = divisor * i;
    i ++;
  }
  return num - ( product - divisor );
}