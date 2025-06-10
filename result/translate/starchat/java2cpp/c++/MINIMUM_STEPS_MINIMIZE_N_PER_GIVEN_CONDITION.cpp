int f_gold ( int n ) {
  vector <int> table ( n + 1, n );
  for ( int i = 0; i <= n; i++ ) {
    for ( int j = i; j > 0; j /= 2 ) {
      if (! (j % 2 > 0)) table[j] = min ( table[j], table[j - 1] + 1 );
      if (! (j % 3 > 0)) table[j] = min ( table[j], table[j - 1] + 1 );
    }
  }
  return table[1];
}