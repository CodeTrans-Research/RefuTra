public static int f_gold ( int [ ] n ) {
  int res = n [ 0 ] ;
  for ( int j = n . length - 1 ;
  j >= 0 ;
  j -- ) {
    res += n [ j ] ;
  }
  return res ;
}
