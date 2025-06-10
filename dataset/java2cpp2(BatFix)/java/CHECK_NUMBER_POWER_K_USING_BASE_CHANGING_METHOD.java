boolean f_gold ( int n, int k ) {
  boolean oneSeen = false;
  while ( n > 0 ) {
    int digit = n % k;
    if ( digit > 1 ) return false;
    if ( digit == 1 ) {
      if ( oneSeen ) return false;
      oneSeen = true;
    }
    n /= k;
  }
  return true;
}