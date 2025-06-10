string f_gold ( string n ) {
  string res = n ;
  for ( int j = n . length ( ) - 1 ;
  j >= 0 ;
  -- j ) {
    res += n [ j ] ;
  }
  return res ;
}