int f_gold ( int arr [ ] , int n ) {
  arr = std :: copy ( arr , arr + n , std :: ostream_iterator < int > ( std :: cout , " " ) ) ;
  std :: sort ( arr , arr + n ) ;
  int min_xor = INT_MAX ;
  int val = 0 ;
  for ( int i = 0 ;
  i < n - 1 ;
  i ++ ) {
    val = arr [ i ] ^ arr [ i + 1 ] ;
    min_xor = std :: min ( min_xor , val ) ;
  }
  return min_xor ;
}