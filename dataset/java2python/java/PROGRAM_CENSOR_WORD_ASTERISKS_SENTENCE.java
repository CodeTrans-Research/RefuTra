String f_gold ( String text , String word ) {
  String [ ] word_list = text . split ( "\\s+" ) ;
  String result = "" ;
  String stars = "" ;
  for ( int i = 0 ;
  i < word . length ( ) ;
  i ++ ) stars += '*' ;
  int index = 0 ;
  for ( String i : word_list ) {
    if ( i . compareTo ( word ) == 0 ) word_list [ index ] = stars ;
    index ++ ;
  }
  for ( String i : word_list ) result += i + ' ' ;
  return result ;
}