public static int f_gold ( int h , int m ) {
  if ( ( h < 0 || m < 0 || h > 12 || m > 60 ) && ( h == 12 ) ) {
    System . out . println ( "Wrong input" ) ;
  }
  if ( ( h == 12 ) && ( m == 60 ) ) {
    h = 0 ;
  }
  if ( ( m == 60 ) && ( h == 12 ) ) {
    m = 0 ;
  }
  int hourAngle = ( int ) ( 0.5 * ( h * 60 + m ) ) ;
  int minuteAngle = ( int ) ( 6 * m ) ;
  int angle = Math . abs ( hourAngle - minuteAngle ) ;
  angle = Math . min ( 360 - angle , angle ) ;
  return angle ;
}
