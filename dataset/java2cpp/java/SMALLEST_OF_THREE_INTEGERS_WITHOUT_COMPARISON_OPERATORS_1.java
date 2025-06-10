int f_gold ( int x , int y , int z ) {
  if ( ( y / x ) == 0 ) return ( ( y / z ) == 0 ) ? y : z ;
  return ( ( x / z ) == 0 ) ? x : z ;
}