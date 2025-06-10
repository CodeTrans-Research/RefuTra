int f_gold ( char X [ ] , char Y [ ] , int l , int r , int k , int dp [ ] [ ] [ ] ) {
  if ( k == 0 ) {
    return 0 ;
  }
  if ( l < 0 | r < 0 ) {
    return ( int ) 1e9 ;
  }
  if ( dp [ l ] [ r ] [ k ] != - 1 ) {
    return dp [ l ] [ r ] [ k ] ;
  }
  int cost = ( X [ l ] - 'a' ) ^ ( Y [ r ] - 'a' ) ;
  return dp [ l ] [ r ] [ k ] = Math . min ( Math . min ( cost + f_gold ( X , Y , l - 1 , r - 1 , k - 1 , dp ) , f_gold ( X , Y , l - 1 , r , k , dp ) ) , f_gold ( X , Y , l , r - 1 , k , dp ) ) ;
}