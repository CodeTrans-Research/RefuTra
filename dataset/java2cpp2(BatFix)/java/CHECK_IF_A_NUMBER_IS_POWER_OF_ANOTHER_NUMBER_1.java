boolean f_gold ( int x, int y ) {
  int res1 = ( int ) Math . log ( y ) / ( int ) Math . log ( x );
  double res2 = Math . log ( y ) / Math . log ( x );
  return ( res1 == res2 );
}