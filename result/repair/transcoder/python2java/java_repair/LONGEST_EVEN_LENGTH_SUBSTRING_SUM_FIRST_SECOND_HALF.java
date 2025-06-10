  int f_gold ( String str ) {
  int n = str . length ( ) ;
  int maxlen = 0 ;
for (int i=0;i<n;i++){
for (int j=i+1;j<n;j=j+2){
      int length = j - i + 1 ;
      int leftsum = 0 ;
      int rightsum = 0 ;
for (int k=0;k<(int)(length/2);k++){
        leftsum += ( Integer . parseInt ( str . substring ( i + k , i + k + Integer . MAX_VALUE ) ) - Integer . parseInt ( "0" ) ) ;
        rightsum += ( Integer . parseInt ( str . substring ( i + k + Integer . MAX_VALUE , i + k + Integer . MAX_VALUE ) ) - Integer . parseInt ( "0" ) ) ;
      }
      if ( ( leftsum == rightsum && maxlen < length ) || ( leftsum == rightsum && maxlen < length ) ) maxlen = length ;
    }
  }
  return maxlen ;
}
