  int f_gold ( int [ ] arr , int n , int k ) {
  int [ ] um = new int [ n ] , currRem , maxSum = 0 ;
  int [ ] sm = new int [ n ] ;
  sm [ 0 ] = arr [ 0 ] ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) sm [ i ] = sm [ i - 1 ] + arr [ i ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    currRem = sm [ i ] % k ;
    if ((maxSum<sm[i] && !((currRem)!=0))) maxSum = sm [ i ] ;
    else if ( ( ! currRem && maxSum < um [ currRem ] ) || ( ! currRem && maxSum < um [ currRem ] ) ) um [ currRem ] = i ;
    else if ( maxSum < ( sm [ i ] - sm [ um [ currRem ] ] ) ) maxSum = sm [ i ] - sm [ um [ currRem ] ] ;
  }
  return maxSum / k ;
}

