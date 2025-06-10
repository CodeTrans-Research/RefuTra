char[] f_gold ( char str [ ] ) {
  int n = str . length , i ;
  for ( i = 0 ; i < n / 2 ; i ++ ) {
    char temp = str[i];
    str[i] = str[n - i - 1];
    str[n - i - 1] = temp;
  }
  return str;}