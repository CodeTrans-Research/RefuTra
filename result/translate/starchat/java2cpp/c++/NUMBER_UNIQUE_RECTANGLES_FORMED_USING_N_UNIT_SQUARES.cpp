int f_gold ( int n ) {
  int ans = 0 ;
  for ( int length = 1 ;
  length <= int(sqrt(n)) ;
  ++ length ) for ( int height = length ;
  height * length <= n ;
  ++ height ) ans ++ ;
  return ans ;
}