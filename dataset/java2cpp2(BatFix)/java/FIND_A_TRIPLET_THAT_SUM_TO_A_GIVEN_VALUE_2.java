boolean f_gold ( int A [ ], int arr_size, int sum ) {
  for ( int i = 0;
  i < arr_size - 2;
  i ++ ) {
    HashSet < Integer > s = new HashSet < Integer > ( );
    int curr_sum = sum - A [ i ];
    for ( int j = i + 1;
    j < arr_size;
    j ++ ) {
      if ( s . contains ( curr_sum - A [ j ] ) && curr_sum - A [ j ] != ( int ) s . toArray ( ) [ s . size ( ) - 1 ] ) {
        System . out . printf ( "Triplet is %d, %d, %d", A [ i ], A [ j ], curr_sum - A [ j ] );
        return true;
      }
      s . add ( A [ j ] );
    }
  }
  return false;
}