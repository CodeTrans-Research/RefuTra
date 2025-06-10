int f_gold ( int notes [ ] , int n ) {
  int five_count = 0 ;
  int ten_count = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( notes [ i ] == 5 ) {
      five_count ++ ;
    }
    else if ( notes [ i ] == 10 ) {
      if ( five_count > 0 ) {
        five_count -- ;
        ten_count ++ ;
      }
      else return 0 ;
    }
    else {
      if ( five_count > 0 && ten_count > 0 ) {
        five_count -- ;
        ten_count -- ;
      }
      else if ( five_count >= 3 ) five_count -= 3 ;
      else return 0 ;
    }
  }
  return 1 ;
}