public static int fGold ( int [ ] arr , int low , int high ) {
  if ( high >= low ) {
    int mid = ( int ) ( low + ( high - low ) / 2 ) ;
    if ( ( ( mid == high || arr [ mid + 1 ] == 0 ) && ( arr [ mid ] == 1 ) ) || ( ( mid == high ) && ( arr [ mid ] == 0 ) ) ) {
      return mid + 1 ;
    }
    if ( arr [ mid ] == 1 ) {
      return fGold ( arr , ( mid + 1 ) , high ) ;
    }
    return fGold ( arr , low , mid - 1 ) ;
  }
  return 0 ;
}