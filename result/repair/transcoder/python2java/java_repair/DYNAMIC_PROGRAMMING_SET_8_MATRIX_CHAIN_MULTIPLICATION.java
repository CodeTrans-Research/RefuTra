double f_gold(double [ ] p,double i,double j){
  if ( i == j ) return 0 ;
  double _min = Integer . MAX_VALUE ;
  for ( double k = i ;
  k < j ;
  k ++ ) {
    double count = ( f_gold ( p , i , k ) + f_gold ( p , k + 1 , j ) + p [ i - 1 ] * p [ k ] * p [ j ] ) ;
    if ( count < _min ) _min = count ;
  }
  return _min ;
}
