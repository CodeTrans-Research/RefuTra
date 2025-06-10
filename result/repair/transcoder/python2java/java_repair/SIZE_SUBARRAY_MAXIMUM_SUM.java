  int f_gold ( int [ ] a , int size ) {
  int maxSo_far = - Integer . MAX_VALUE - 1 ;
  int maxending_here = 0 ;
  int start = 0 ;
  int end = 0 ;
  int s = 0 ;
for (int i=0;i<size;i++){
    maxending_here += a [ i ] ;
    if ( maxSo_far < maxending_here ) {
      maxSo_far = maxending_here ;
      start = s ;
      end = i ;
    }
    if ( maxending_here < 0 ) {
      maxending_here = 0 ;
      s = i + 1 ;
    }
  }
  return ( end - start + 1 ) ;
}
