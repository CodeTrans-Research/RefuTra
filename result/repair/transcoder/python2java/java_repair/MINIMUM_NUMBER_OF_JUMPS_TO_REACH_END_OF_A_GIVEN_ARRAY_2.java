  int f_gold ( int [ ] arr , int n ) {
  int [ ] jumps = new int [ n ] ;
for (int i=n-2;i>-1;i--){
    if ( ( arr [ i ] == 0 ) && ( arr [ i ] != 1 ) ) {
      jumps [ i ] = Integer.MAX_VALUE;
    }
    else if ( arr [ i ] >= n - i - 1 ) {
      jumps [ i ] = 1 ;
    }
    else {
      int min = Integer.MAX_VALUE;
      for ( int j = i + 1 ;
      j < n ;
      j ++ ) {
        if ( j <= arr [ i ] + i ) {
          if ( min > jumps [ j ] ) {
            min = jumps [ j ] ;
          }
        }
      }
            if (min!=Integer.MAX_VALUE ) {
        jumps [ i ] = min + 1 ;
      }
      else {
        jumps [ i ] = min ;
      }
    }
  }
  return jumps [ 0 ] ;
}

