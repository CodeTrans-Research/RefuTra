string f_gold ( string str ) {
  int n = str . size ( ) ;
  string arr [ n ] ;
  string concat = str + str ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) arr [ i ] = concat . substr ( i , n - i ) ;
  sort ( arr , arr + n ) ;
  return arr [ 0 ] ;
}