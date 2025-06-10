int f_gold ( string str [ ], int n ) {
  unordered_map < string, int > m;
  for ( int i = 0 ; i < n ; i ++ ) {
    if ( m.find ( str[i] )!= m.end ( ) ) {
      int get = m[str[i]];
      m[str[i]] = get + 1;
    }
    else {
      m[str[i]] = 1;
    }
  }
  int res = 0;
  for ( auto it : m ) {
    if ( it.second == 2 ) res++;
  }
  return res;
}