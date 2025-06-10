int f_gold ( int ar [ ], int n ) {
  if ( n <= 4 ) return Arrays . stream ( ar ) . min ( ) . getAsInt ( );
  int [ ] sum = new int [ n ];
  sum [ 0 ] = ar [ 0 ];
  sum [ 1 ] = ar [ 1 ];
  sum [ 2 ] = ar [ 2 ];
  sum [ 3 ] = ar [ 3 ];
  for ( int i = 4;
  i < n;
  i ++ ) sum [ i ] = ar [ i ] + Arrays . stream ( Arrays . copyOfRange ( sum, i - 4, i ) ) . min ( ) . getAsInt ( );
  return Arrays . stream ( Arrays . copyOfRange ( sum, n - 4, n ) ) . min ( ) . getAsInt ( );
}