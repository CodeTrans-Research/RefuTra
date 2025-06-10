  int f_gold ( int a , int b ) {
  if ( a < 0 ) a = - a ;
  if ( b < 0 ) b = - b ;
  int mod = a ;
  while (mod>=b)mod = mod - b ;
  if ( a < 0 ) return - mod ;
  return mod ;
}

