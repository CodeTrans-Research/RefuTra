  int f_gold ( int n ) {
  int count = 0 ;
  for ( int curr = 0 ;
  curr < Integer . MAX_VALUE ;
  curr ++ ) {
    int sum = 0 ;
    int x = curr ;
    while ( ( x = curr ) != 0 ) {
      sum = sum + x % 10 ;
      x = x / 10 ;
    }
    if ( sum == 10 ) {
      count = count + 1 ;
    }
    if ( ( count == n ) && ( count == n ) ) {
      return curr ;
    }
  }
  return - 1 ;
}

