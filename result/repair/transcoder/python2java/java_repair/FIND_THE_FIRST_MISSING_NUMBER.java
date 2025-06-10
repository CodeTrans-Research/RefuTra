  int f_gold ( int [ ] array , int start , int end ) {
  if ( ( start > end ) || ( end > array . length ) ) return end + 1 ;
  if ( start != array [ start ] ) return start ;
  ;
  int mid = ( int ) ( ( start + end ) / 2 ) ;
  if ( ( array [ mid ] == mid ) || ( array [ mid ] == end ) ) return f_gold ( array , mid + 1 , end ) ;
  return f_gold ( array , start , mid ) ;
}

