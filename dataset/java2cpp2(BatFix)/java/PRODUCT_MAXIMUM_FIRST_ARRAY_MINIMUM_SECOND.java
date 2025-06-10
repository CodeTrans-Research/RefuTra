int f_gold ( int arr1 [ ], int arr2 [ ], int n1, int n2 ) {
  Arrays . sort ( arr1 );
  Arrays . sort ( arr2 );
  return arr1 [ n1 - 1 ] * arr2 [ 0 ];
}