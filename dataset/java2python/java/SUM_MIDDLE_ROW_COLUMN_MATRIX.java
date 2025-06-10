void f_gold ( int mat [ ] [ ] , int n ) {
  int row_sum = 0 , col_sum = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) row_sum += mat [ n / 2 ] [ i ] ;
  System . out . println ( "Sum of middle row = " + row_sum ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) col_sum += mat [ i ] [ n / 2 ] ;
  System . out . println ( "Sum of middle column = " + col_sum ) ;
}