public static int f_gold ( int [ ] arr , int n ) {
  HashMap < Integer , Integer > um = new HashMap < Integer , Integer > ( ) ;
  int sum = 0 ;
  int maxLen = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( arr [ i ] == 0 ) {
      sum ++ ;
    }
    else {
      sum ++ ;
    }
    if ( ( sum == 1 ) && ( ( i - 1 ) < n ) ) {
      maxLen = i + 1 ;
    }
    else if ( ( sum != 0 ) && ( ( i - 1 ) < n ) ) {
      um . put ( sum , i ) ;
    }
    if ( ( ( sum - 1 ) < n ) && ( ( i - 1 ) < n ) ) {
      if ( ( maxLen < ( i - um . get ( sum - 1 ) ) ) && ( ( i - um . get ( sum - 1 ) ) < n ) ) {
        maxLen = i - um . get ( sum - 1 ) ;
      }
    }
  }
  return maxLen ;
}
