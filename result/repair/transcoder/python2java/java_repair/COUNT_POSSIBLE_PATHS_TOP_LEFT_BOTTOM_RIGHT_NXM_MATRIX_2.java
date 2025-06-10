  int f_gold ( int p , int q ) {
  int [ ] dp = new int [ q ] ;
  dp [ 0 ] = 1 ;
for (int i=0;i<p;i++){
    for ( int j = 1 ;
    j < q ;
    j ++ ) {
      dp [ j ] += dp [ j - 1 ] ;
    }
  }
  return dp [ q - 1 ] ;
}
