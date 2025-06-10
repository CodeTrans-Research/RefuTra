int f_gold ( int A [ ], int B [ ], int m, int n ) {
  Arrays . sort ( A );
  Arrays . sort ( B );
  int a = 0, b = 0;
  int result = Integer . MAX_VALUE;
  while ( a < m && b < n ) {
    if ( Math . abs ( A [ a ] - B [ b ] ) < result ) result = Math . abs ( A [ a ] - B [ b ] );
    if ( A [ a ] < B [ b ] ) a ++;
    else b ++;
  }
  return result;
}