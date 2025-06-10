int f_gold ( String str, int len ) {
  int count = 1;
  if ( len == 1 ) return count;
  if ( str . charAt ( 0 ) == str . charAt ( 1 ) ) count *= 1;
  else count *= 2;
  for ( int j = 1;
  j < len - 1;
  j ++ ) {
    if ( str . charAt ( j ) == str . charAt ( j - 1 ) && str . charAt ( j ) == str . charAt ( j + 1 ) ) count *= 1;
    else if ( str . charAt ( j ) == str . charAt ( j - 1 ) || str . charAt ( j ) == str . charAt ( j + 1 ) || str . charAt ( j - 1 ) == str . charAt ( j + 1 ) ) count *= 2;
    else count *= 3;
  }
  if ( str . charAt ( len - 1 ) == str . charAt ( len - 2 ) ) count *= 1;
  else count *= 2;
  return count;
}