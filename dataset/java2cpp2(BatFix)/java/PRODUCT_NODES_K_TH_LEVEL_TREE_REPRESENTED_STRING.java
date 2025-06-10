int f_gold ( String tree, int k ) {
  int level = - 1;
  int product = 1;
  int n = tree . length ( );
  for ( int i = 0;
  i < n;
  i ++ ) {
    if ( tree . charAt ( i ) == '(' ) level ++;
    else if ( tree . charAt ( i ) == ')' ) level --;
    else {
      if ( level == k ) product *= ( tree . charAt ( i ) - '0' );
    }
  }
  return product;
}