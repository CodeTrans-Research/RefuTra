int f_gold ( String num, int a ) {
  int res = 0;
  for ( int i = 0;
  i < num . length ( );
  i ++ ) res = ( res * 10 + ( int ) num . charAt ( i ) - '0' ) % a;
  return res;
}