public static int f_gold ( double x , double y ) {
  int res1 = ( int ) ( Math . log ( y ) / Math . log ( x ) ) ;
  int res2 = Math . log ( y ) / Math . log ( x ) ;
  return 1 == ( res1 == res2 ) ? 0 : 1 ;
}