  boolean f_gold ( int [ ] arr , int n , int x ) {
  if ( n < 2 ) return false ;
  HashSet s = new HashSet ( ) ;
for (int i=0;i<n;i++){
    if ( arr [ i ] == 0 ) {
      if ( x == 0 ) return true ;
      else continue ;
    }
    if ( x % arr [ i ] == 0 ) {
      if ( x / arr [ i ] < s . size ( ) ) return true ;
      s . add ( arr [ i ] ) ;
    }
  }
  return false ;
}

