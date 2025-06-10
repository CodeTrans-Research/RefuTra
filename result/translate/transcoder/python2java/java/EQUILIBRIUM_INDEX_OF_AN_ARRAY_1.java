public static int f_gold ( int [ ] arr , int n ) {
  int totalSum = sum ( arr ) ;
  int leftsum = 0 ;
  for ( int i = 0 , num = arr . length ;
  i < n ;
  i ++ ) {
    totalSum -= num ;
    if ( leftsum == totalSum ) {
      return i ;
    }
    leftsum += num ;
  }
  return - 1 ;
}