int f_gold ( int m, int n ) {
  int **T = new int *[m + 1];
  for (int i = 0; i <= m; i++)
    T[i] = new int[n + 1];
  for ( int i = 0 ;
  i < m + 1 ;
  i ++ ) {
    for ( int j = 0 ;
    j < n + 1 ;
    j ++ ) {
      if ( i == 0 || j == 0 ) T [ i ] [ j ] = 0 ;
      else if ( i < j ) T [ i ] [ j ] = 0 ;
      else if ( j == 1 ) T [ i ] [ j ] = i ;
      else T [ i ] [ j ] = T [ i - 1 ] [ j ] + T [ i / 2 ] [ j - 1 ] ;
    }
  }
  int ans = T [ m ] [ n ] ;
  for (int i = 0; i <= m; i++)
    delete [] T[i];
  delete [] T;
  return ans ;
}