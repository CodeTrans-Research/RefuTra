boolean f_gold ( int n ) {
  if ( n <= 1 ) System . out . println ( "False" );
  if ( n <= 3 ) System . out . println ( "False" );
  if ( n % 2 == 0 || n % 3 == 0 ) return true;
  for ( int i = 5;
  i * i <= n;
  i = i + 6 ) if ( n % i == 0 || n % ( i + 2 ) == 0 ) return true;
  return false;
}