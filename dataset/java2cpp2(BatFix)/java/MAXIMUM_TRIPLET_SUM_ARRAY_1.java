int f_gold ( int arr [ ], int n ) {
  Arrays . sort ( arr );
  return arr [ n - 1 ] + arr [ n - 2 ] + arr [ n - 3 ];
}