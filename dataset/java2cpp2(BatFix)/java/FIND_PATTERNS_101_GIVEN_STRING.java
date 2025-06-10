int f_gold ( String str ) {
  char last = str . charAt ( 0 );
  int i = 1, counter = 0;
  while ( i < str . length ( ) ) {
    if ( str . charAt ( i ) == '0' && last == '1' ) {
      while ( str . charAt ( i ) == '0' ) i ++;
      if ( str . charAt ( i ) == '1' ) counter ++;
    }
    last = str . charAt ( i );
    i ++;
  }
  return counter;
}