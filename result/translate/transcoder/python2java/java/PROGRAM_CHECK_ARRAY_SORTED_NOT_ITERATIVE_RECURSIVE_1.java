public static boolean f_gold ( int [ ] arr , int n ) {
  if ( ( n == 0 || n == 1 ) && ( arr [ 0 ] > arr [ 1 ] ) ) return true ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) if ( ( arr [ i - 1 ] > arr [ i ] ) && ( arr [ i ] > arr [ i ] ) ) return false ;
  return true ;
}
