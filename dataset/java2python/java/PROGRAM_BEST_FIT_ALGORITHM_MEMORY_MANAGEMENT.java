void f_gold ( int blockSize [ ] , int m , int processSize [ ] , int n ) {
  int allocation [ ] = new int [ n ] ;
  for ( int i = 0 ;
  i < allocation . length ;
  i ++ ) allocation [ i ] = - 1 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    int bestIdx = - 1 ;
    for ( int j = 0 ;
    j < m ;
    j ++ ) {
      if ( blockSize [ j ] >= processSize [ i ] ) {
        if ( bestIdx == - 1 ) bestIdx = j ;
        else if ( blockSize [ bestIdx ] > blockSize [ j ] ) bestIdx = j ;
      }
    }
    if ( bestIdx != - 1 ) {
      allocation [ i ] = bestIdx ;
      blockSize [ bestIdx ] -= processSize [ i ] ;
    }
  }
  System . out . println ( "\nProcess No.\tProcess Size\tBlock no." ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    System . out . print ( "   " + ( i + 1 ) + "\t\t" + processSize [ i ] + "\t\t" ) ;
    if ( allocation [ i ] != - 1 ) System . out . print ( allocation [ i ] + 1 ) ;
    else System . out . print ( "Not Allocated" ) ;
    System . out . println ( ) ;
  }
}