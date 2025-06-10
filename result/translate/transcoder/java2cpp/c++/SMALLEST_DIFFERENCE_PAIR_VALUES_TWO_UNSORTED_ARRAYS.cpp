int f_gold ( int A [ ] , int B [ ] , int m , int n ) {
  A = std :: copy ( A , A + m , A + m + n ) ;
  B = std :: copy ( B , B + n , B + n + m ) ;
  std :: sort ( A , A + m , std :: greater < int > ( ) ) ;
  std :: sort ( B , B + n , std :: greater < int > ( ) ) ;
  int a = 0 , b = 0 ;
  int result = INT_MAX ;
  while ( a < m && b < n ) {
    if ( std :: abs ( A [ a ] - B [ b ] ) < result ) {
      result = std :: abs ( A [ a ] - B [ b ] ) ;
    }
    if ( A [ a ] < B [ b ] ) {
      a ++ ;
    }
    else {
      b ++ ;
    }
  }
  return result ;
}