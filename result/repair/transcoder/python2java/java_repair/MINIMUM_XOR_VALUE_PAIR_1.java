  int f_gold ( int [ ] arr , int n ) {
  int [ ] array = new int [ n ] ;
  Arrays . fill ( array , 0 ) ;
  int minXor = Integer . MAX_VALUE ;
  int val ;
for (int i=0;i<n-1;i++){
    val = array [ i ] ^ array [ i + 1 ] ;
    ;
    minXor = Math . min ( minXor , val ) ;
    ;
  }
  return minXor ;
}
