int f_gold ( int arr [ ] , int n ) {
  vector < int > s ;
  int j = 0 ;
  int ans = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    while ( j < n && ! s . empty ( ) ) {
      s . push_back ( arr [ j ] ) ;
      j ++ ;
    }
    ans += ( ( j - i ) * ( j - i + 1 ) ) / 2 ;
    s . erase ( vector < int > ( arr , arr + i ) ) ;
  }
  return ans ;
}