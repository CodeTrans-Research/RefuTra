int f_gold ( int A [ ], int B [ ], int m, int n ) {
  A = Arrays.copyOfRange( A, 0, m );
  B = Arrays.copyOfRange( B, 0, n );
  sort ( A, 0, m-1 );
  sort ( B, 0, n-1 );
  int a = 0, b = 0 ;
  int result = INT_MAX ;
  while ( a < m && b < n ) {
    if ( abs ( A [ a ] - B [ b ] ) < result ) result = abs ( A [ a ] - B [ b ] ) ;
    if ( A [ a ] < B [ b ] ) a ++ ;
    else b ++ ;
  }
  return result ;
}