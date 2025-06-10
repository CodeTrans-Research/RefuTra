public static int f_gold ( int [ ] cost , int n , int W ) {
  List < Integer > val = Arrays . asList ( ) ;
  List < Integer > wt = Arrays . asList ( ) ;
  int size = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( ( cost [ i ] != - 1 ) && ( cost [ i ] != 0 ) ) {
      val . add ( cost [ i ] ) ;
      wt . add ( i + 1 ) ;
      size ++ ;
    }
  }
  n = size ;
  int [ ] [ ] minCost = new int [ W + 1 ] [ n + 1 ] ;
  for ( int j = 0 ;
  j < n + 1 ;
  j ++ ) {
    minCost [ 0 ] [ j ] = Integer . MAX_VALUE ;
  }
  for ( int i = 1 ;
  i <= n ;
  i ++ ) {
    minCost [ i ] [ 0 ] = 0 ;
  }
  for ( int i = 1 ;
  i <= n ;
  i ++ ) {
    for ( int j = 1 ;
    j <= W ;
    j ++ ) {
      if ( ( wt [ i - 1 ] > j ) && ( wt [ i ] > wt [ j ] ) ) {
        minCost [ i ] [ j ] = minCost [ i - 1 ] [ j ] ;
      }
      else {
        minCost [ i ] [ j ] = Math . min ( minCost [ i - 1 ] [ j ] , minCost [ i ] [ j - wt [ i - 1 ] ] + val . get ( i - 1 ) ) ;
      }
    }
  }
  if ( ( minCost [ n ] [ W ] == Integer . MAX_VALUE ) && ( minCost [ n ] [ W ] == 0 ) ) {
    return - 1 ;
  }
  else {
    return minCost [ n ] [ W ] ;
  }
}