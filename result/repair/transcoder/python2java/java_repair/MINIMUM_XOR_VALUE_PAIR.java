  int f_gold ( int [ ] arr , int n ) {
  int minXor = 999999 ;
  int val ;
for (int i=0;i<n;i++){
for (int j=i+1;j<n;j++){
      val = arr [ i ] ^ arr [ j ] ;
      minXor = Math . min ( minXor , val ) ;
    }
  }
  return minXor ;
}
