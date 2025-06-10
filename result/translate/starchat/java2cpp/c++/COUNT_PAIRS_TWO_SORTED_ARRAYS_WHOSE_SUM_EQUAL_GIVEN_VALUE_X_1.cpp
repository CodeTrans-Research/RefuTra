int f_gold ( int arr1 [ ], int arr2 [ ], int m, int n, int x ) {
  int count = 0 ;
  set < int > s;
  for ( int i = 0 ; i < m ; i ++ ) s.insert ( arr1 [ i ] ) ;
  for ( int j = 0 ; j < n ; j ++ ) if ( s.find ( x - arr2 [ j ] )!= s.end ( ) ) count ++ ;
  return count ;
}