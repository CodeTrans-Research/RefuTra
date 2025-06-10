public static int f_gold ( int [ ] arr , int n ) {
  int [ ] jumps = new int [ n ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( ( arr [ i ] == 0 ) && ( arr [ i ] != 1 ) ) {
      jumps [ i ] = Integer . MIN_VALUE ;
    }
    else if ( ( arr [ i ] >= n - i - 1 ) && ( arr [ i ] != 0 ) ) {
      jumps [ i ] = 1 ;
    }
    else {
      int min = Integer . MIN_VALUE ;
      for ( int j = i + 1 ;
      j < n ;
      j ++ ) {
        if ( ( j <= arr [ i ] + i ) && ( arr [ j ] != 0 ) ) {
          if ( ( min > jumps [ j ] ) || ( min < jumps [ j ] ) ) {
            min = jumps [ j ] ;
          }
        }
      }
      if ( ( min != Integer . MIN_VALUE ) && ( jumps [ i ] != 0 ) ) {
        jumps [ i ] = min + 1 ;
      }
      else {
        jumps [ i ] = min ;
      }
    }
  }
  return jumps [ 0 ] ;
}
