int f_gold ( int [ ] arr, int n ) {
  Queue < Integer > q = new LinkedList < > ( );
  Arrays . sort ( arr );
  q . add ( arr [ 0 ] );
  for ( int i = 1;
  i < n;
  i ++ ) {
    int now = q . element ( );
    if ( arr [ i ] >= 2 * now ) q . remove ( );
    q . add ( arr [ i ] );
  }
  return q . size ( );
}