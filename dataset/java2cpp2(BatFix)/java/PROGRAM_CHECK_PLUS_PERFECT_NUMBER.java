boolean f_gold ( int x ) {
  int temp = x;
  int n = 0;
  while ( x != 0 ) {
    x /= 10;
    n ++;
  }
  x = temp;
  int sum = 0;
  while ( x != 0 ) {
    sum += Math . pow ( x % 10, n );
    x /= 10;
  }
  return ( sum == temp );
}