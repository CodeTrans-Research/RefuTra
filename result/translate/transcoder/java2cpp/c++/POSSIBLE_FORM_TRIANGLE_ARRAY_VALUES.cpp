bool f_gold ( int * arr , int N ) {
  arr = std :: copy ( arr , arr + N , std :: ostream_iterator < int > ( std :: cout , " " ) ) ;
  if ( N < 3 ) return false ;
  std :: sort ( arr , arr + N ) ;
  for ( int i = 0 ;
  i < N - 2 ;
  i ++ ) if ( arr [ i ] + arr [ i + 1 ] > arr [ i + 2 ] ) return true ;
  return false ;
}