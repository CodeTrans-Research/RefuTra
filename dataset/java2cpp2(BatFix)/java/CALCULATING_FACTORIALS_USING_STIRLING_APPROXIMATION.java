int f_gold ( double n ) {
  if ( n == 1 ) return 1;
  double z;
  double e = 2.71;
  z = Math . sqrt ( 2 * 3.14 * n ) * Math . pow ( ( n / e ), n );
  return ( int ) ( z );
}