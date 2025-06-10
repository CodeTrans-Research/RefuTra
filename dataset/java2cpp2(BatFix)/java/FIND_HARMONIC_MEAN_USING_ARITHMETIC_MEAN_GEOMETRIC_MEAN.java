double f_gold ( int a, int b ) {
  double AM, GM, HM;
  AM = ( a + b ) / 2;
  GM = Math . sqrt ( a * b );
  HM = ( GM * GM ) / AM;
  return HM;
}