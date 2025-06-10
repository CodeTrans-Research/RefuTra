void f_gold ( char s1 [ ], char s2 [ ], int index ) {
  s2 [ index ] = s1 [ index ];
  if ( index == s1 . length - 1 ) {
    return;
  }
  f_gold ( s1, s2, index + 1 );
}