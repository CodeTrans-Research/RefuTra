boolean f_gold ( int arr1 [ ], int arr2 [ ], int m, int n ) {
  int i = 0, j = 0;
  if ( m < n ) return false;
  Arrays . sort ( arr1 );
  Arrays . sort ( arr2 );
  while ( i < n && j < m ) {
    if ( arr1 [ j ] < arr2 [ i ] ) j ++;
    else if ( arr1 [ j ] == arr2 [ i ] ) {
      j ++;
      i ++;
    }
    else if ( arr1 [ j ] > arr2 [ i ] ) return false;
  }
  if ( i < n ) return false;
  else return true;
}