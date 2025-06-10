int f_gold ( int limit ) {
  if ( limit < 2 ) return 0 ;
  long ef1 = 0, ef2 = 2 ;
  long sum = ef1 + ef2 ;
  while ( ef2 <= limit ) {
    long ef3 = 4 * ef2 + ef1 ;
    if ( ef3 > limit ) break ;
    ef1 = ef2 ;
    ef2 = ef3 ;
    sum += ef2 ;
  }
  return ( int ) sum ;
}