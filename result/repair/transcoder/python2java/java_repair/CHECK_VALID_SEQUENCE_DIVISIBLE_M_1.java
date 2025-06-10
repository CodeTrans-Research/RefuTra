  boolean f_gold ( int n , int index , int modulo , int M , int [ ] arr , int [ ] [ ] dp ) {
  modulo = ( ( modulo % M ) + M ) % M ;
  if ( index == n ) {
    if ( ( modulo == 0 ) ) return 1 ;
    return 0 ;
  }
  if ( ( dp [ index ] [ modulo ] != - 1 ) && ( dp [ index ] [ modulo ] != - 1 ) ) return dp [ index ] [ modulo ] ;
  boolean placeAdd = f_gold ( n , index + 1 , modulo + arr [ index ] , M , arr , dp ) ;
  boolean placeMinus = f_gold ( n , index + 1 , modulo - arr [ index ] , M , arr , dp ) ;
  boolean res = ( Boolean ) placeAdd || placeMinus ;
  dp [ index ] [ modulo ] = res ;
  return res ;
}

