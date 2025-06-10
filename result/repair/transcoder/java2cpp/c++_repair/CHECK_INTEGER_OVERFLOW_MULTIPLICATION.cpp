bool f_gold(unsigned long a,unsigned long b){
  if ( a == 0 || b == 0 ) return false ;
  unsigned long result = a * b ;
  if ( a == result / b ) return false ;
  else return true ;
}
