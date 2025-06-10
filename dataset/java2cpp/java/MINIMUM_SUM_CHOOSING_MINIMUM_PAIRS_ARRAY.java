int f_gold ( int [ ] A , int n ) {
  int min_val = Arrays . stream ( A ) . min ( ) . getAsInt ( ) ;
  return ( min_val * ( n - 1 ) ) ;
}