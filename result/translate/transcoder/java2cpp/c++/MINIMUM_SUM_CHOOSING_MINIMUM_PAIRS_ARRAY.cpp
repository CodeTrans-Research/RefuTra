int f_gold ( vector < int > & A , int n ) {
  int min_val = std :: min ( A . begin ( ) , A . end ( ) ) ;
  return ( min_val * ( n - 1 ) ) ;
}