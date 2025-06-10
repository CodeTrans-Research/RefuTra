int f_gold ( int pages [ ], int n, int capacity ) {
  HashSet < Integer > s = new HashSet < > ( capacity );
  Queue < Integer > indexes = new LinkedList < > ( );
  int page_faults = 0;
  for ( int i = 0;
  i < n;
  i ++ ) {
    if ( s . size ( ) < capacity ) {
      if ( ! s . contains ( pages [ i ] ) ) {
        s . add ( pages [ i ] );
        page_faults ++;
        indexes . add ( pages [ i ] );
      }
    }
    else {
      if ( ! s . contains ( pages [ i ] ) ) {
        int val = indexes . peek ( );
        indexes . poll ( );
        s . remove ( val );
        s . add ( pages [ i ] );
        indexes . add ( pages [ i ] );
        page_faults ++;
      }
    }
  }
  return page_faults;
}