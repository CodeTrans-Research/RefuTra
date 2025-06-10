int f_gold ( int arr [ ] , int n ) {
  unordered_map < int , int > hm ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( hm . count ( arr [ i ] ) ) {
      hm [ arr [ i ] ] = hm [ arr [ i ] ] + 1 ;
    }
    else {
      hm [ arr [ i ] ] = 1 ;
    }
  }
  int ans = 0 ;
  for ( auto it = hm . begin ( ) ;
  it != hm . end ( ) ;
  ++ it ) {
    int count = * it ;
    ans += ( count * ( count - 1 ) ) / 2 ;
  }
  return ans ;
}