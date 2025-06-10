public static int f_gold ( String num ) {
  int n = num . length ( ) ;
  int [ ] sumofdigit = new int [ n ] ;
  sumofdigit [ 0 ] = ( int ) ( num . charAt ( 0 ) - '0' ) ;
  int res = sumofdigit [ 0 ] ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    int numi = ( int ) ( num . charAt ( i ) - '0' ) ;
    sumofdigit [ i ] = ( i + 1 ) + numi + 10 + sumofdigit [ i - 1 ] ;
    res += sumofdigit [ i ] ;
  }
  return res ;
}