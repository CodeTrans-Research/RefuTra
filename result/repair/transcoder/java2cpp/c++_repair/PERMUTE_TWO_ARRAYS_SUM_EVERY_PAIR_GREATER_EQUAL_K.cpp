bool f_gold(int a [],int32_t b [],int n,int k){
  a = std :: copy ( a , a + n , std :: ostream_iterator < int32_t > ( std :: cout , " " ) ) ;
  b = std :: copy ( b , b + n , std :: ostream_iterator < int32_t > ( std :: cout , " " ) ) ;
  std :: sort ( a , a + n , std :: greater < int32_t > ( ) ) ;
  std :: sort ( b , b + n , std :: greater < int32_t > ( ) ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) if ( a [ i ] + b [ i ] < k ) return false ;
  return true ;
}
