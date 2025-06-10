boolean f_gold ( int p ) {
  Long checkNumber = (long) Math . pow ( 2 , p ) - 1 ;
  Long nextval = 4 % checkNumber ;
  for ( int i = 1 ;
  i < p - 1 ;
  i ++ ) nextval = ( nextval * nextval - 2 ) % checkNumber ;
  return ( nextval == 0 ) ;
}