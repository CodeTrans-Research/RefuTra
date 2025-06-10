public static int f_filled ( int [ ] high , int [ ] low , int n ) {
  if ( ( n <= 0 ) || ( n > ( high . length - 1 ) ) ) return 0 ;
  return Math . max ( high [ n - 1 ] + f_filled ( high , low , ( n - 2 ) ) , low [ n - 1 ] + f_filled ( high , low , ( n - 1 ) ) ) ;
  ;
}
