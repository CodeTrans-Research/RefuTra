public static double f_gold ( double l ) {
  double leafNodeCount = Math . pow ( 2 , l - 1 ) ;
  double sumLastLevel ;
  sumLastLevel = ( ( leafNodeCount * ( leafNodeCount + 1 ) ) / 2 ) ;
  double sum = sumLastLevel * l ;
  return sum ;
}