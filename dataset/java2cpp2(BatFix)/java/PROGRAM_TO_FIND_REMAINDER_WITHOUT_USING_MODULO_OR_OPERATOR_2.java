int f_gold ( int num, int divisor ) {
  while ( num >= divisor ) num -= divisor;
  return num;
}