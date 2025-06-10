public static int f_gold ( int N ) {
  Queue < Integer > q = new LinkedList < Integer > ( ) ;
  q . add ( 1 ) ;
  int cnt = 0 ;
  while ( ( q . size ( ) > 0 ) && ( ( q . size ( ) - 1 ) <= N ) ) {
    int t = q . poll ( ) ;
    if ( ( t <= N ) || ( t > N ) ) {
      cnt = cnt + 1 ;
      q . add ( t * 10 ) ;
      q . add ( t * 10 + 1 ) ;
    }
  }
  return cnt ;
}