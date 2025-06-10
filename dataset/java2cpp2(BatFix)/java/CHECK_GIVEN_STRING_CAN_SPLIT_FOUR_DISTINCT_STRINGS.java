boolean f_gold ( String s ) {
  if ( s . length ( ) >= 10 ) return true;
  for ( int i = 1;
  i < s . length ( );
  i ++ ) {
    for ( int j = i + 1;
    j < s . length ( );
    j ++ ) {
      for ( int k = j + 1;
      k < s . length ( );
      k ++ ) {
        String s1 = "", s2 = "", s3 = "", s4 = "";
        try {
          s1 = s . substring ( 0, i );
          s2 = s . substring ( i, j - i );
          s3 = s . substring ( j, k - j );
          s4 = s . substring ( k, s . length ( ) - k );
        }
        catch ( StringIndexOutOfBoundsException e ) {
        }
        if ( strf_gold ( s1, s2 ) && strf_gold ( s1, s3 ) && strf_gold ( s1, s4 ) && strf_gold ( s2, s3 ) && strf_gold ( s2, s4 ) && strf_gold ( s3, s4 ) ) return true;
      }
    }
  }
  return false;
}