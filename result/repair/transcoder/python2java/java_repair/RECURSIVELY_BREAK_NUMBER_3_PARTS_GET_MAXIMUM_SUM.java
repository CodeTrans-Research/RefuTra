  int f_gold ( int n ) {
  if ( n == 0 || n == 1 ) return n ;
  return Math . max ( ( f_gold ( n / 2 ) + f_gold ( n / 3 ) + f_gold ( n / 4 ) ) , n ) ;
}

