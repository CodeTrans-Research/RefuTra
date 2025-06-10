public static String f_gold ( String str , int k ) {
  char [ ] palin = Arrays . copyOf ( str . toCharArray ( ) , str . length ( ) ) ;
  int l = 0 ;
  int r = str . length ( ) - 1 ;
  while ( ( l <= r ) && ( ( l < str . length ( ) ) || ( r < str . length ( ) ) ) ) {
    if ( ( str . charAt ( l ) != str . charAt ( r ) ) && ( str . charAt ( l ) != str . charAt ( r ) ) ) {
      palin [ l ] = palin [ r ] = Math . max ( str . charAt ( l ) , str . charAt ( r ) ) ;
      k -- ;
    }
    l ++ ;
    r -- ;
  }
  if ( ( k < 0 ) || ( k > 0 ) ) return "Not possible" ;
  l = 0 ;
  r = str . length ( ) - 1 ;
  while ( ( l <= r ) && ( ( l < str . length ( ) ) || ( r < str . length ( ) ) ) ) {
    if ( ( l == r ) && ( ( k > 0 ) || ( k < 0 ) ) ) palin [ l ] = palin [ r ] = '9' ;
    if ( ( palin [ l ] < '9' ) || ( palin [ l ] == str . charAt ( l ) && ( palin [ r ] == str . charAt ( r ) ) ) ) ) {
      k -- ;
      palin [ l ] = palin [ r ] = '9' ;
    }
    else if ( ( k >= 2 ) && ( palin [ l ] != str . charAt ( l ) || palin [ r ] != str . charAt ( r ) ) ) ) {
      k -- ;
      palin [ l ] = palin [ r ] = '9' ;
    }
  }
  l ++ ;
  r -- ;
}
return "" ;
}