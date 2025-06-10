long f_gold ( int n ) {
  long sum = 0;
  for ( int row = 0;
  row < n;
  row ++ ) {
    sum = sum + ( 1 << row );
  }
  return sum;
}