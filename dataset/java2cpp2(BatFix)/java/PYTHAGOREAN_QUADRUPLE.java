Boolean f_gold ( int a, int b, int c, int d ) {
  int sum = a * a + b * b + c * c;
  if ( d * d == sum ) return true;
  else return false;
}