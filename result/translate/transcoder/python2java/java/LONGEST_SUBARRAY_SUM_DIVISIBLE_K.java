public static int f_gold ( int [ ] arr , int n , int k ) {
  HashMap < Integer , Integer > um = new HashMap < Integer , Integer > ( ) ;
  int [ ] mod_arr = new int [ n ] ;
  int max = 0 ;
  int currSum = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    currSum += arr [ i ] ;
    mod_arr [ i ] = ( ( currSum % k ) + k ) % k ;
  }
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( ( mod_arr [ i ] == 0 ) && ( mod_arr [ i ] < um . size ( ) ) ) {
      max = i + 1 ;
    }
    else if ( ( mod_arr [ i ] < um . size ( ) ) && ( mod_arr [ i ] > um . size ( ) ) ) {
      um . put ( mod_arr [ i ] , i ) ;
    }
    else {
      if ( ( max < ( i - um . get ( mod_arr [ i ] ) ) ) && ( mod_arr [ i ] > um . size ( ) ) ) {
        max = i - um . get ( mod_arr [ i ] ) ;
      }
    }
  }
  return max ;
}