boolean f_gold ( String str1, String str2, int m, int n ) {
  int j = 0;
  for ( int i = 0;
  i < n && j < m;
  i ++ ) if ( str1 . charAt ( j ) == str2 . charAt ( i ) ) j ++;
  return ( j == m );
}