int f_gold ( int C, int l ) {
  if ( l >= C ) return C;
  double eq_root = ( Math . sqrt ( 1 + 8 * ( C - l ) ) - 1 ) / 2;
  return ( int ) ( Math . ceil ( eq_root ) + l );
}