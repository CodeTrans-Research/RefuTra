  int f_gold ( int n ) {
  int k = n ;
  int imin = 1 ;
  int ans = 0 ;
  while (imin<=n){
    int imax = ( int ) ( n / k ) ;
    ans += k * ( imax - imin + 1 ) ;
    imin = imax + 1 ;
    k = ( int ) ( n / imin ) ;
  }
  return ans ;
}
