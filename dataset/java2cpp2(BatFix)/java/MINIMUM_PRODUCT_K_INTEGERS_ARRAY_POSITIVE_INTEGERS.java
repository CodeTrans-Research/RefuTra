int f_gold ( int [ ] arr, int n, int k ) {
  PriorityQueue < Integer > pq = new PriorityQueue < > ( );
  for ( int i = 0;
  i < n;
  i ++ ) pq . add ( arr [ i ] );
  int count = 0, ans = 1;
  while ( pq . isEmpty ( ) == false && count < k ) {
    ans = ans * pq . element ( );
    pq . remove ( );
    count ++;
  }
  return ans;
}