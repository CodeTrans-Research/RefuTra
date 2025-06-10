  int f_gold ( int [ ] A , int [ ] B , int m , int n ) {
  A = A . clone ( ) ;
  B = B . clone ( ) ;
  A . sort ( ) ;
  B . sort ( ) ;
  int a = 0 ;
  int b = 0 ;
  int result = Integer . MAX_VALUE ;
  while (a<m&&b<n){
    if ( ( Math . abs ( A [ a ] - B [ b ] ) < result ) || ( Math . abs ( A [ a ] - B [ b ] ) < result ) ) {
      result = Math . abs ( A [ a ] - B [ b ] ) ;
    }
    if (A[a] < B[b]) {
      a ++ ;
    }
    else {
      b ++ ;
    }
  }
  return result ;
}
