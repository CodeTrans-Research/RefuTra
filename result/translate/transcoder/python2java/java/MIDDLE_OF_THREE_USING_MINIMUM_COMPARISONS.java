public static int f_gold ( int a , int b , int c ) {
  if ( ( ( a < b && b < c ) || ( c < b && b < a ) ) && ( ( b < a && a < c ) || ( c < a && a < b ) ) ) return b ;
  ;
  if ( ( ( b < a && a < c ) || ( c < a && a < b ) ) && ( ( c < a && a < b ) || ( c < a && a < c ) ) && ( ( a < b && b < c ) || ( a < b && b < c ) ) && ( ( b < a && a < c ) || ( b < a && c < c ) ) && ( ( c < a && a < b ) || ( c < a && c < b ) || ( c < a && c < b ) || ( c < a && c < b ) || ( c < a && c < b ) ) ) return c ;
  else return c ;
}
