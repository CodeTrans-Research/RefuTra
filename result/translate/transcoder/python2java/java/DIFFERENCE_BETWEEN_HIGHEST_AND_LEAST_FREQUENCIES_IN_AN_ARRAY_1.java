public static int f_gold ( int [ ] arr , int n ) {
  TreeMap < Integer , Integer > mp = new TreeMap < Integer , Integer > ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    mp . put ( arr [ i ] , 0 ) ;
  }
  int maxCount = 0 ;
  int minCount = n ;
  for ( Map . Entry < Integer , Integer > entry : mp . entrySet ( ) ) {
    maxCount = Math . max ( maxCount , entry . getValue ( ) ) ;
    minCount = Math . min ( minCount , entry . getValue ( ) ) ;
  }
  return maxCount - minCount ;
}