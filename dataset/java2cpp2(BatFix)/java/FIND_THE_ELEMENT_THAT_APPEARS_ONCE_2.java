int f_gold ( int a [ ], int n ) {
  HashSet < Integer > s = new HashSet < Integer > ( );
  for ( int i : a ) {
    s . add ( i );
  }
  int arr_sum = 0;
  for ( int i : a ) {
    arr_sum += i;
  }
  int set_sum = 0;
  for ( int i : s ) {
    set_sum += i;
  }
  return ( 3 * set_sum - arr_sum ) / 2;
}