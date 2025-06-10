String f_gold ( String n ) {
  String res = n;
  for ( int j = n . length ( ) - 1;
  j >= 0;
  -- j ) res += n . charAt ( j );
  return res;
}