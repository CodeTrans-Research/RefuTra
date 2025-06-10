int f_gold ( int arr [ ] , int n , int num , int max_limit ) {
  int ind ;
  int val ;
  int dp [ n ] [ max_limit + 1 ] ;
  for ( ind = 0 ;
  ind < n ;
  ind ++ ) {
    for ( val = 0 ;
    val <= max_limit ;
    val ++ ) {
      if ( ind == 0 ) {
        if ( num - arr [ ind ] == val || num + arr [ ind ] == val ) dp [ ind ] [ val ] = 1 ;
        else dp [ ind ] [ val ] = 0 ;
      }
      else {
        if ( val - arr [ ind ] >= 0 && val + arr [ ind ] <= max_limit ) {
          if ( dp [ ind - 1 ] [ val - arr [ ind ] ] == 1 || dp [ ind - 1 ] [ val + arr [ ind ] ] == 1 ) {
            dp [ ind ] [ val ] = 1 ;
          }
        }
        else if ( val - arr [ ind ] >= 0 ) {
          dp [ ind ] [ val ] = dp [ ind - 1 ] [ val - arr [ ind ] ] ;
        }
        else if ( val + arr [ ind ] <= max_limit ) {
          dp [ ind ] [ val ] = dp [ ind - 1 ] [ val + arr [ ind ] ] ;
        }
        else {
          dp [ ind ] [ val ] = 0 ;
        }
      }
    }
  }
  for ( val = max_limit ;
  val >= 0 ;
  val -- ) {
    if ( dp [ n - 1 ] [ val ] == 1 ) return val ;
  }
  return - 1 ;
}