  String f_gold ( int n ) {
  if ( n == 0 ) return "0" ;
  ;
  String bin = "" ;
  ;
  while ( ( n > 0 ) && ( n & 1 == 0 ) ) {
    if ( ( n & 1 == 0 ) ) bin = "0" + bin ;
    else bin = "1" + bin ;
    n = n >> 1 ;
  }
  return bin ;
}

