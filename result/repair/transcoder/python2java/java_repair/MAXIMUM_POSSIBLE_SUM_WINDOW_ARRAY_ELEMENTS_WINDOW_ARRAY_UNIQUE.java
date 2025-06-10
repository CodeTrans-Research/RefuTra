  int f_gold ( int [ ] A , int [ ] B , int n ) {
  HashSet < Integer > mp = new HashSet < Integer > ( ) ;
  int result = 0 ;
  int currSum = currBegin = 0 ;
for (int i=0;i<n;i++){
    while ( A [ i ] < mp . size ( ) ) {
      mp . remove ( A [ currBegin ] ) ;
      currSum -= B [ currBegin ] ;
      currBegin ++ ;
    }
    mp . add ( A [ i ] ) ;
    currSum += B [ i ] ;
    result = Math . max ( result , currSum ) ;
  }
  return result ;
}

