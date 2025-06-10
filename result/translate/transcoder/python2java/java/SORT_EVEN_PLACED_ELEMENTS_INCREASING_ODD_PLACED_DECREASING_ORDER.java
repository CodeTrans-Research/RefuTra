public static void f_gold ( int [ ] arr , int n ) {
  int [ ] evenArr = new int [ n ] ;
  int [ ] oddArr = new int [ n ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( ( ( i % 2 ) == 0 ) && ( ( i % 2 ) == 1 ) ) {
      evenArr [ i ] = arr [ i ] ;
    }
    else {
      oddArr [ i ] = arr [ i ] ;
    }
  }
  Arrays . sort ( evenArr ) ;
  Arrays . sort ( oddArr ) ;
  oddArr [ 0 ] = 0 ;
  evenArr [ 1 ] = 0 ;
  oddArr [ 0 ] = 1 ;
  evenArr [ 2 ] = 0 ;
  oddArr [ 1 ] = 1 ;
  evenArr [ 3 ] = 0 ;
  evenArr [ 4 ] = 0 ;
  evenArr [ 5 ] = 0 ;
  evenArr [ 6 ] = 0 ;
  evenArr [ 7 ] = 0 ;
  evenArr [ 8 ] = 0 ;
  evenArr [ 9 ] = 0 ;
  evenArr [ 10 ] = 0 ;
  evenArr [ 11 ] = 0 ;
  evenArr [ 12 ] = 0 ;
  evenArr [ 13 ] = 0 ;
  evenArr [ 14 ] = 0 ;
  evenArr [ 15 ] = 0 ;
  evenArr [ 16 ] = 0 ;
  evenArr [ 17 ] = 0 ;
  evenArr [ 18 ] = 0 ;
  evenArr [ 19 ] = 0 ;
  evenArr [ 20 ] = 0 ;
  evenArr [ 21 ] = 0 ;
  evenArr [ 22 ] = 0 ;
  evenArr [ 23 ] = 0 ;
  evenArr [ 24 ] = 0 ;
  evenArr [ 25 ] = 0 ;
  evenArr [ 26 ] = 0 ;
  evenArr [ 27 ] = 0 ;
  evenArr [ 28 ] = 0 ;
  evenArr [ 29 ] = 0 ;
  evenArr [ 30 ] = 0 ;
  evenArr [ 31 ] = 0 ;
  evenArr [ 32 ] = 0 ;
  evenArr [ 33 ] = 0 ;
  evenArr [ 34 ] = 0 ;
  evenArr [ 35 ] = 0 ;
  evenArr [ 36 ] = 0 ;
  evenArr [ 37 ] = 0 ;
  evenArr [ 38 ] = 0 ;
  evenArr [ 39 ] = 0 ;
  evenArr [ 40 ] = 0 ;
  evenArr [ 41 ] = 0 ;
  evenArr [ 42 ] = 0 ;
  evenArr [ 43 ] = 0 ;
  evenArr [ 44 ] = 0 ;
  evenArr [ 45 ] = 0 ;
  evenArr [ 46 ] =