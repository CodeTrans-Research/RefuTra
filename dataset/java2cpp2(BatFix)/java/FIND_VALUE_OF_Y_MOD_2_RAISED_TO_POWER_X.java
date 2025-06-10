long f_gold ( long y, long x ) {
  if ( ( Math . log ( y ) / Math . log ( 2 ) ) < x ) return y;
  if ( x > 63 ) return y;
  return ( y % ( 1 << ( int ) x ) );
}