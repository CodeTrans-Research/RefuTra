int f_gold ( int arr [ ], int n, int m ) {
  int max = 0, min = 0;
  Arrays . sort ( arr );
  for ( int i = 0, j = n - 1;
  i < m;
  i ++, j -- ) {
    min += arr [ i ];
    max += arr [ j ];
  }
  return ( max - min );
}