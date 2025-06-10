  int f_gold ( int [ ] arr , int n ) {
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    int j = 0 ;
    while (j<n){
      if ( i != j && arr [ i ] == arr [ j ] ) {
        break ;
      }
      j ++ ;
    }
    if ( j == n ) {
      return arr [ i ] ;
    }
  }
  return - 1 ;
}

