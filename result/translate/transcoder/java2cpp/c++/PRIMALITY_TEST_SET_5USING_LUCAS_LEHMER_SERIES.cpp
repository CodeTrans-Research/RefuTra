bool f_gold ( int p ) {
  int64_t checkNumber = ( int64_t ) pow ( 2 , p ) - 1 ;
  int64_t nextval = 4 % checkNumber ;
  for ( int i = 1 ;
  i < p - 1 ;
  i ++ ) {
    nextval = ( nextval * nextval - 2 ) % checkNumber ;
  }
  return ( nextval == 0 ) ;
}