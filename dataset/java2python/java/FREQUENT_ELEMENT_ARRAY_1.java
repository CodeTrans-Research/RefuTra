int f_gold ( int arr [ ] , int n ) {
  Map < Integer , Integer > hp = new HashMap < Integer , Integer > ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    int key = arr [ i ] ;
    if ( hp . containsKey ( key ) ) {
      int freq = hp . get ( key ) ;
      freq ++ ;
      hp . put ( key , freq ) ;
    }
    else {
      hp . put ( key , 1 ) ;
    }
  }
  int max_count = 0 , res = - 1 ;
  for ( Entry < Integer , Integer > val : hp . entrySet ( ) ) {
    if ( max_count < val . getValue ( ) ) {
      res = val . getKey ( ) ;
      max_count = val . getValue ( ) ;
    }
  }
  return res ;
}