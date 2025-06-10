public static int f_gold ( int x , int y , int z ) {
  if ( ( ! Integer . isNegativeVInt ( y / x ) ) && ( ! Integer . isNegativeVInt ( y / z ) ) ) {
    return y == 0 ? 0 : z ;
  }
  return x == 0 ? 0 : z ;
}