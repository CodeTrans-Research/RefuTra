String f_gold ( String str , int n ) {
  String reverseAlphabet = "zyxwvutsrqponmlkjihgfedcba" ;
  int l = str . length ( ) ;
  String answer = "" ;
  for ( int i = 0 ; i < n ; i ++ ) {
    if ( i < l ) answer = answer + str . charAt ( i ) ;
  }
  for ( int i = n ;
  i < l ;
  i ++ ) answer = answer + reverseAlphabet . charAt ( str . charAt ( i ) - 'a' ) ;
  return answer ;
}