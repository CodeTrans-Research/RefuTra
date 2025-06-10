public static int f_gold ( int [ ] ar , int arSize ) {
  int res = 0 ;
  for ( int i = 0 ;
  i != arSize ;
  i ++ ) {
    res = res ^ ar [ i ] ;
  }
  return res ;
}