String f_gold ( double num, int k_prec ) {
  String binary = "";
  int Integral = ( int ) num;
  double fractional = num - Integral;
  while ( Integral > 0 ) {
    int rem = Integral % 2;
    binary += ( ( char ) ( rem + '0' ) );
    Integral /= 2;
  }
  binary = reverse ( binary );
  binary += ( '.' );
  while ( k_prec -- > 0 ) {
    fractional *= 2;
    int fract_bit = ( int ) fractional;
    if ( fract_bit == 1 ) {
      fractional -= fract_bit;
      binary += ( char ) ( 1 + '0' );
    }
    else {
      binary += ( char ) ( 0 + '0' );
    }
  }
  return binary;
}