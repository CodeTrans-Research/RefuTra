String f_gold ( String X, String Y ) {
  int m = X . length ( );
  int n = Y . length ( );
  int dp [ ] [ ] = new int [ m + 1 ] [ n + 1 ];
  for ( int i = 0;
  i <= m;
  i ++ ) {
    for ( int j = 0;
    j <= n;
    j ++ ) {
      if ( i == 0 ) {
        dp [ i ] [ j ] = j;
      }
      else if ( j == 0 ) {
        dp [ i ] [ j ] = i;
      }
      else if ( X . charAt ( i - 1 ) == Y . charAt ( j - 1 ) ) {
        dp [ i ] [ j ] = 1 + dp [ i - 1 ] [ j - 1 ];
      }
      else {
        dp [ i ] [ j ] = 1 + Math . min ( dp [ i - 1 ] [ j ], dp [ i ] [ j - 1 ] );
      }
    }
  }
  int index = dp [ m ] [ n ];
  String str = "";
  int i = m, j = n;
  while ( i > 0 && j > 0 ) {
    if ( X . charAt ( i - 1 ) == Y . charAt ( j - 1 ) ) {
      str += ( X . charAt ( i - 1 ) );
      i --;
      j --;
      index --;
    }
    else if ( dp [ i - 1 ] [ j ] > dp [ i ] [ j - 1 ] ) {
      str += ( Y . charAt ( j - 1 ) );
      j --;
      index --;
    }
    else {
      str += ( X . charAt ( i - 1 ) );
      i --;
      index --;
    }
  }
  while ( i > 0 ) {
    str += ( X . charAt ( i - 1 ) );
    i --;
    index --;
  }
  while ( j > 0 ) {
    str += ( Y . charAt ( j - 1 ) );
    j --;
    index --;
  }
  str = reverse ( str );
  return str;
}