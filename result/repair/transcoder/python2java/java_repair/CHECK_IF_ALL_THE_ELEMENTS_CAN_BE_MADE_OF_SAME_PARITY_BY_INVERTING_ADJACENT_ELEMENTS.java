  boolean f_gold ( int [ ] a , int n ) {
  int countOdd = 0 ;
  int countEven = 0 ;
  ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( ( a [ i ] & 1 ) != 0 ) {
      countOdd ++ ;
    }
    else {
      countEven ++ ;
    }
  }
  if (((countEven%2)!=0 && (countOdd%2)!=0)) {
    return false ;
  }
  else {
    return true ;
  }
}

