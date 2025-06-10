int f_gold ( int N ) {
  Queue < Integer > q = new LinkedList < > ( );
  q . add ( 1 );
  int cnt = 0;
  int t;
  while ( q . size ( ) > 0 ) {
    t = q . peek ( );
    q . remove ( );
    if ( t <= N ) {
      cnt ++;
      q . add ( t * 10 );
      q . add ( t * 10 + 1 );
    }
  }
  return cnt;
}