public static boolean f_gold ( String string ) {
  Stack < Character > stack = new Stack < Character > ( ) ;
  for ( char ch : string . toCharArray ( ) ) {
    if ( ch == ')' ) {
      char top = stack . pop ( ) ;
      int elementsInside = 0 ;
      while ( top != '(' ) {
        elementsInside ++ ;
        top = stack . pop ( ) ;
      }
      if ( elementsInside < 1 ) {
        return true ;
      }
    }
    else {
      stack . push ( ch ) ;
    }
  }
  return false ;
}
