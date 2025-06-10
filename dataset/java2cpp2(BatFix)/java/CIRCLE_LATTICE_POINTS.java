int f_gold ( int r ) {
  if ( r <= 0 ) return 0;
  int result = 4;
  for ( int x = 1;
  x < r;
  x ++ ) {
    int ySquare = r * r - x * x;
    int y = ( int ) Math . sqrt ( ySquare );
    if ( y * y == ySquare ) result += 4;
  }
  return result;
}