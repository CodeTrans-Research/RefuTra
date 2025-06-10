int f_gold ( int arr [ ], int n, int x ) {
  int i = 0;
  while ( i < n ) {
    if ( arr [ i ] == x ) return i;
    i = i + Math . abs ( arr [ i ] - x );
  }
  System . out . println ( "number is not" + " present!" );
  return - 1;
}