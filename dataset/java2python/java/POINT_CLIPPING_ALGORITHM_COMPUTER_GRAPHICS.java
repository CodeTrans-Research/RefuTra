void f_gold ( int XY [ ] [ ] , int n , int Xmin , int Ymin , int Xmax , int Ymax ) {
  System . out . printf ( "Point inside the viewing pane:\n" ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( ( XY [ i ] [ 0 ] >= Xmin ) && ( XY [ i ] [ 0 ] <= Xmax ) ) {
      if ( ( XY [ i ] [ 1 ] >= Ymin ) && ( XY [ i ] [ 1 ] <= Ymax ) ) System . out . printf ( "[%d, %d] " , XY [ i ] [ 0 ] , XY [ i ] [ 1 ] ) ;
    }
  }
  System . out . printf ( "\nPoint outside the viewing pane:\n" ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( ( XY [ i ] [ 0 ] < Xmin ) || ( XY [ i ] [ 0 ] > Xmax ) ) System . out . printf ( "[%d, %d] " , XY [ i ] [ 0 ] , XY [ i ] [ 1 ] ) ;
    if ( ( XY [ i ] [ 1 ] < Ymin ) || ( XY [ i ] [ 1 ] > Ymax ) ) System . out . printf ( "[%d, %d] " , XY [ i ] [ 0 ] , XY [ i ] [ 1 ] ) ;
  }
}