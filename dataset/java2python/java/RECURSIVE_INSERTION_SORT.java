void f_gold ( int arr [ ] , int n ) {
  if ( n <= 1 ) return ;
  f_gold ( arr , n - 1 ) ;
  int last = arr [ n - 1 ] ;
  int j = n - 2 ;
  while ( j >= 0 && arr [ j ] > last ) {
    arr [ j + 1 ] = arr [ j ] ;
    j -- ;
  }
  arr [ j + 1 ] = last ;
}