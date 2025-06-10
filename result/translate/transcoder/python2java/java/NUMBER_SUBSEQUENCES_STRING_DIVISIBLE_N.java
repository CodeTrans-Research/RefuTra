public static int f_gold ( String str , int n ) {
  int l = str . length ( ) ;
  int [ ] [ ] dp = new int [ n ] [ l ] ;
  for ( int y = 0 ;
  y < l ;
  y ++ ) {
    dp [ 0 ] [ ( ( int ) str . charAt ( 0 ) - '0' ) % n ] ++ ;
    for ( int i = 1 ;
    i < l ;
    i ++ ) {
      dp [ i ] [ ( ( int ) str . charAt ( i ) - '0' ) % n ] ++ ;
      for ( int j = 0 ;
      j < n ;
      j ++ ) {
        dp [ i ] [ j ] += dp [ i - 1 ] [ j ] ;
        dp [ i ] [ ( j * 10 + ( int ) str . charAt ( i ) - '0' ) ] += dp [ i - 1 ] [ j ] ;
      }
    }
  }
  return dp [ l - 1 ] [ 0 ] ;
}