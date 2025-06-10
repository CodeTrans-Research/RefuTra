int f_gold ( int arr [ ], int n ) {
  unordered_map < int, int > mp;
  for ( int i = 0 ; i < n ; i ++ ) {
    if ( mp.find ( arr[i] )!= mp.end ( ) ) mp[arr[i]]++;
    else mp[arr[i]] = 1;
  }
  int max_count = 0, min_count = n;
  for ( auto x : mp ) {
    max_count = max ( max_count, x.second );
    min_count = min ( min_count, x.second );
  }
  return ( max_count - min_count );
}