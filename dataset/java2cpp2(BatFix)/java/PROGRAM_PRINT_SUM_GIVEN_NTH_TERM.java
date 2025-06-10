int f_gold ( long n ) {
  int S = 0;
  for ( i = 1;
  i <= n;
  i ++ ) S += i * i - ( i - 1 ) * ( i - 1 );
  return S;
}