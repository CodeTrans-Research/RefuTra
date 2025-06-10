int f_gold ( int * a , int n ) {
  a = std :: copy ( a , a + n , std :: ostream_iterator < int > ( std :: cout , " " ) ) ;
  std :: sort ( a , a + n ) ;
  int sum = 0 ;
  bool flag = false ;
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