int f_gold ( String str ) {
  String temp = "";
  int sum = 0;
  for ( int i = 0;
  i < str . length ( );
  i ++ ) {
    char ch = str . charAt ( i );
    if ( Character . isDigit ( ch ) ) temp += ch;
    else {
      sum += Integer . parseInt ( temp );
      temp = "0";
    }
  }
  return sum + Integer . parseInt ( temp );
}