int f_gold ( String n ) {
  int k = 0, pos = 0, i = 0;
  while ( k != n . length ( ) ) {
    switch ( n . charAt ( i ) ) {
      case '4' : pos = pos * 2 + 1;
      break;
      case '7' : pos = pos * 2 + 2;
      break;
    }
    i ++;
    k ++;
  }
  return pos;
}