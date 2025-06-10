boolean f_gold ( String str1, String str2, int m, int n ) {
  if ( m == 0 ) return true;
  if ( n == 0 ) return false;
  if ( str1 . charAt ( m - 1 ) == str2 . charAt ( n - 1 ) ) return f_gold ( str1, str2, m - 1, n - 1 );
  return f_gold ( str1, str2, m, n - 1 );
}