public static int f_gold ( int [ ] a , int n ) {
  int [ ] a = new int [ n ] ;
  Arrays . sort ( a ) ;
  int sum = 0 ;
  boolean flag = false ;
  int len = 0 ;
  int i = 0 ;
  while ( ( i < n - 1 ) && ( ( a [ i ] == a [ i + 1 ] || a [ i ] - a [ i + 1 ] == 1 ) && flag == false ) ) {
    if ( ( ( a [ i ] == a [ i + 1 ] || a [ i ] - a [ i + 1 ] == 1 ) && flag == true ) ) {
      flag = true ;
      len = a [ i + 1 ] ;
      i = i + 1 ;
    }
    else if ( ( ( a [ i ] == a [ i + 1 ] || a [ i ] - a [ i + 1 ] == 1 ) && flag == true ) ) {
      sum = sum + a [ i + 1 ] * len ;
      flag = false ;
      i = i + 1 ;
    }
    i ++ ;
  }
  return sum ;
}