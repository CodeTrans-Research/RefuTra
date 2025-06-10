public static int f_gold ( int [ ] arr , int x ) {
  int n = arr . length ;
  for ( int j = 0 ;
  j != n ;
  j ++ ) {
    if ( ( x == arr [ j ] ) && ( x != 0 ) ) {
      return j ;
    }
  }
  return - 1 ;
}