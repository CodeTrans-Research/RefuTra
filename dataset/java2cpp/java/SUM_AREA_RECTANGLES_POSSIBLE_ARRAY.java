int f_gold ( int [ ] a , int n ) {
  a = Arrays.copyOfRange( a , 0 , n );
  Arrays . sort ( a ) ;
  int sum = 0 ;
  boolean flag = false ;
  int len = 0 ;
  for ( int i = 0 ;
  i < n - 1 ;
  i ++ ) {
    if ( ( a [ i ] == a [ i + 1 ] || a [ i ] - a [ i + 1 ] == 1 ) && ! flag ) {
      flag = true ;
      len = a [ i + 1 ] ;
      i ++ ;
    }
    else if ( ( a [ i ] == a [ i + 1 ] || a [ i ] - a [ i + 1 ] == 1 ) && ( flag ) ) {
      sum = sum + a [ i + 1 ] * len ;
      flag = false ;
      i ++ ;
    }
  }
  return sum ;
}