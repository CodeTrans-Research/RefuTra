int f_gold ( int arr [ ], int n ) {
  HashSet < Integer > us = new HashSet < > ( );
  int even_count = 0;
  for ( int i = 0;
  i < n;
  i ++ ) if ( arr [ i ] % 2 == 0 ) us . add ( arr [ i ] );
  even_count = us . size ( );
  return ( int ) ( Math . pow ( 2, even_count ) - 1 );
}