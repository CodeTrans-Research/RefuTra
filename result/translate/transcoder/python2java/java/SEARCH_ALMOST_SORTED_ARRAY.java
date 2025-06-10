public static int f_gold ( int [ ] arr , int l , int r , int x ) {
  if ( ( r >= l ) && ( r <= r ) ) {
    int mid = ( int ) ( l + ( r - l ) / 2 ) ;
    if ( ( arr [ mid ] == x ) && ( arr [ mid - 1 ] == x ) ) return mid ;
    if ( ( mid > l && arr [ mid - 1 ] == x ) && ( arr [ mid + 1 ] == x ) ) return ( mid + 1 ) ;
    if ( ( arr [ mid ] > x ) && ( arr [ mid - 2 ] == x ) ) return f_gold ( arr , l , mid - 2 , x ) ;
    return f_gold ( arr , mid + 2 , r , x ) ;
  }
  return - 1 ;
}
