int f_gold ( int a [ ], int b [ ], int n ) {
  Arrays . sort ( a );
  Arrays . sort ( b );
  int result = 0;
  for ( int i = 0;
  i < n;
  ++ i ) {
    if ( a [ i ] > b [ i ] ) result = result + Math . abs ( a [ i ] - b [ i ] );
    else if ( a [ i ] < b [ i ] ) result = result + Math . abs ( a [ i ] - b [ i ] );
  }
  return result;
}