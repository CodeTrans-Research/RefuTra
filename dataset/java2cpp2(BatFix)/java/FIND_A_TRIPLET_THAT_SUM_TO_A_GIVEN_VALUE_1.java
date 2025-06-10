boolean f_gold ( int A [ ], int arr_size, int sum ) {
  int l, r;
  quickSort ( A, 0, arr_size - 1 );
  for ( int i = 0;
  i < arr_size - 2;
  i ++ ) {
    l = i + 1;
    r = arr_size - 1;
    while ( l < r ) {
      if ( A [ i ] + A [ l ] + A [ r ] == sum ) {
        System . out . print ( "Triplet is " + A [ i ] + ", " + A [ l ] + ", " + A [ r ] );
        return true;
      }
      else if ( A [ i ] + A [ l ] + A [ r ] < sum ) l ++;
      else r --;
    }
  }
  return false;
}