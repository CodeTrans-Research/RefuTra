double f_gold ( double p ) {
  return Math . ceil ( Math . sqrt ( 2 * 365 * Math . log ( 1 / ( 1 - p ) ) ) );
}