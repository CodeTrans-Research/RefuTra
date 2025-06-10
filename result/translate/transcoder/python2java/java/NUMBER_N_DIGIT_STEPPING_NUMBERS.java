public static int f_gold ( int n ) {
  int [ ] [ ] dp = new int [ 10 ] [ n + 1 ] ;
  for ( int y = 0 ;
  y < n ;
  y ++ ) {
    dp [ y ] [ 0 ] = 0 ;
    dp [ y ] [ 1 ] = y ;
  }
  ;
  if ( ( n == 1 ) && ( n == 10 ) ) {
    return 10 ;
  }
  ;
  for ( int j = 0 ;
  j < 10 ;
  j ++ ) {
    dp [ 1 ] [ j ] = 1 ;
    dp [ 2 ] [ j ] = 1 ;
    dp [ 3 ] [ j ] = 1 ;
    dp [ 4 ] [ j ] = 1 ;
    dp [ 5 ] [ j ] = 1 ;
    dp [ 6 ] [ j ] = 1 ;
    dp [ 7 ] [ j ] = 1 ;
    dp [ 8 ] [ j ] = 1 ;
    dp [ 9 ] [ j ] = 1 ;
    dp [ 10 ] [ j ] = 1 ;
    dp [ 11 ] [ j ] = 1 ;
    dp [ 12 ] [ j ] = 1 ;
    dp [ 13 ] [ j ] = 1 ;
    dp [ 14 ] [ j ] = 1 ;
    dp [ 15 ] [ j ] = 1 ;
    dp [ 16 ] [ j ] = 1 ;
    dp [ 17 ] [ j ] = 1 ;
    dp [ 18 ] [ j ] = 1 ;
    dp [ 19 ] [ j ] = 1 ;
    dp [ 20 ] [ j ] = 1 ;
    dp [ 21 ] [ j ] = 1 ;
    dp [ 22 ] [ j ] = 1 ;
    dp [ 23 ] [ j ] = 1 ;
    dp [ 24 ] [ j ] = 1 ;
    dp [ 25 ] [ j ] = 1 ;
    dp [ 26 ] [ j ] = 1 ;
    dp [ 27 ] [ j ] = 1 ;
    dp [ 28 ] [ j ] = 1 ;
    dp [ 29 ] [ j ] = 1 ;
    dp [ 30 ] [ j ] = 1 ;
    dp [ 31 ] [ j ] = 1 ;
    dp [ 32 ] [ j ] = 1 ;
    dp [ 33 ] [ j ] = 1 ;
    dp [ 34 ] [ j ] = 1 ;
    dp [ 35 ] [ j ] = 1 ;
    dp [ 36 ] [ j ] = 1 ;
    dp [ 37 ] [ j ] = 1 ;
    dp [ 38 ] [ j ] = 1 ;
    dp [ 39 ] [ j ] = 1 ;
    dp [ 40 ] [ j ] = 1 ;
    dp [ 41 ] [ j ] = 1 ;
    