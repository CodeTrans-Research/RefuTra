boolean f_gold ( int ip [ ], int op [ ], int n ) {
  Queue < Integer > input = new LinkedList < > ( );
  for ( int i = 0;
  i < n;
  i ++ ) {
    input . add ( ip [ i ] );
  }
  Queue < Integer > output = new LinkedList < > ( );
  for ( int i = 0;
  i < n;
  i ++ ) {
    output . add ( op [ i ] );
  }
  Stack < Integer > tempStack = new Stack < > ( );
  while ( ! input . isEmpty ( ) ) {
    int ele = input . poll ( );
    if ( ele == output . peek ( ) ) {
      output . poll ( );
      while ( ! tempStack . isEmpty ( ) ) {
        if ( tempStack . peek ( ) == output . peek ( ) ) {
          tempStack . pop ( );
          output . poll ( );
        }
        else break;
      }
    }
    else {
      tempStack . push ( ele );
    }
  }
  return ( input . isEmpty ( ) && tempStack . isEmpty ( ) );
}