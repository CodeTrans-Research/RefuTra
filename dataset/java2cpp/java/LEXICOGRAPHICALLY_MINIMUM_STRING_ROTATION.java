String f_gold ( String str ) {
  int n = str . length ( ) ;
  String arr [ ] = new String [ n ] ;
  String concat = str + str ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    arr [ i ] = concat . substring ( i , i + n ) ;
  }
  Arrays . sort ( arr ) ;
  return arr [ 0 ] ;
}