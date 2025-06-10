int f_gold ( char arr [ ], int n, int k ) {
  int res = 0;
  ArrayList < Integer > thi = new ArrayList < Integer > ( );
  ArrayList < Integer > pol = new ArrayList < Integer > ( );
  for ( int i = 0;
  i < n;
  i ++ ) {
    if ( arr [ i ] == 'P' ) pol . add ( i );
    else if ( arr [ i ] == 'T' ) thi . add ( i );
  }
  int l = 0, r = 0;
  while ( l < thi . size ( ) && r < pol . size ( ) ) {
    if ( Math . abs ( thi . get ( l ) - pol . get ( r ) ) <= k ) {
      res ++;
      l ++;
      r ++;
    }
    else if ( thi . get ( l ) < pol . get ( r ) ) l ++;
    else r ++;
  }
  return res;
}