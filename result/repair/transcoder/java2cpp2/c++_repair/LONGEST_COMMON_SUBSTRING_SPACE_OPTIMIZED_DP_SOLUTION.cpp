int f_gold ( string X , string Y ) {
  int m = X . size ( ) ;
  int n = Y . size ( ) ;
  int result = 0 ;
  int * * len = new int * [ 2 ] ;
for(int i0 = 0;i0 < 2;i0++) len[i0] = new int [n]();
  int currRow = 0 ;
  for ( int i = 0 ;
  i < m ;
  i ++ ) {
    for ( int j = 0 ;
    j < n ;
    j ++ ) {
      if ( i == 0 || j == 0 ) len [ currRow ] [ j ] = 0 ;
      else if ( X [ i - 1 ] == Y [ j - 1 ] ) {
        len [ currRow ] [ j ] = len [ ( 1 - currRow ) ] [ ( j - 1 ) ] + 1 ;
        result = max ( result , len [ currRow ] [ j ] ) ;
      }
      else len [ currRow ] [ j ] = 0 ;
    }
    currRow = 1 - currRow ;
  }
  return result ;
}
