  boolean f_gold ( int n ) {
  if ( n == 0 ) return false ;
  while (n!=1){
    if ( ( n % 4 != 0 ) || ( n % 4 != 1 ) ) return false ;
    n = n / 4 ;
  }
  return true ;
}

