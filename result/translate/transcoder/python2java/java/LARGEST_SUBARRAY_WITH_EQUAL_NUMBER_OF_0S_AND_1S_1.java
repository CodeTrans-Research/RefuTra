public static int f_gold ( int [ ] arr , int n ) {
  HashMap < Integer , Integer > hashMap = new HashMap < Integer , Integer > ( ) ;
  int currSum = 0 ;
  int maxLen = 0 ;
  int endingIndex = - 1 ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    if ( ( arr [ i ] == 0 ) && ( arr [ i ] != - 1 ) ) {
      arr [ i ] = - 1 ;
    }
    else {
      arr [ i ] = 1 ;
    }
  }
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    currSum = currSum + arr [ i ] ;
    if ( ( currSum == 0 ) && ( arr [ i ] != - 1 ) ) {
      maxLen = i + 1 ;
      endingIndex = i ;
    }
    if ( ( currSum + n ) < hashMap . size ( ) ) {
      if ( maxLen < i - hashMap . get ( currSum + n ) ) {
        maxLen = i - hashMap . get ( currSum + n ) ;
        endingIndex = i ;
      }
    }
    else {
      hashMap . put ( currSum + n , i ) ;
    }
  }
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    if ( ( arr [ i ] == - 1 ) && ( arr [ i ] != 0 ) ) {
      arr [ i ] = 0 ;
    }
    else {
      arr [ i ] = 1 ;
    }
  }
  System . out . print ( endingIndex - maxLen + " " ) ;
  System . out . print ( "to" ) ;
  System . out . print ( endingIndex ) ;
  return maxLen ;
}