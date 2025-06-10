int f_gold ( double h, double m ) {
  if ( h < 0 || m < 0 || h > 12 || m > 60 ) System . out . println ( "Wrong input" );
  if ( h == 12 ) h = 0;
  if ( m == 60 ) m = 0;
  int hour_angle = ( int ) ( 0.5 * ( h * 60 + m ) );
  int minute_angle = ( int ) ( 6 * m );
  int angle = Math . abs ( hour_angle - minute_angle );
  angle = Math . min ( 360 - angle, angle );
  return angle;
}