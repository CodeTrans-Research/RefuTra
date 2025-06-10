int f_gold ( int x ) {
  int res = 0 ;
  int count = 0 ;
  count ++ ;
  if ( count == 1 ) res = x ;
  else {
    Random r = new Random ( ) ;
    int i = r . nextInt ( count ) ;
    if ( i == count - 1 ) res = x ;
  }
  return res ;
}