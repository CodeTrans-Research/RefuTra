int f_gold ( int [ ] [ ] [ ] dp , int [ ] arr1 , int n , int [ ] arr2 , int m , int k ) {
  if ( k < 0 ) return - 10000000 ;
  if ( n < 0 || m < 0 ) return 0 ;
  int ans = dp [ n ] [ m ] [ k ] ;
  if ( ans != - 1 ) return ans ;
  try {
    ans = Math . max ( f_gold ( dp , arr1 , n - 1 , arr2 , m , k ) , f_gold ( dp , arr1 , n , arr2 , m - 1 , k ) ) ;
    if ( arr1 [ n - 1 ] == arr2 [ m - 1 ] ) ans = Math . max ( ans , 1 + f_gold ( dp , arr1 , n - 1 , arr2 , m - 1 , k ) ) ;
    ans = Math . max ( ans , 1 + f_gold ( dp , arr1 , n - 1 , arr2 , m - 1 , k - 1 ) ) ;
  }
  catch ( Exception e ) {
  }
  return ans ;
}