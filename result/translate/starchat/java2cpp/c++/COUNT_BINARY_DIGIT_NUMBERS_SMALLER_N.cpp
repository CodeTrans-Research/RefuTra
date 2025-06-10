int f_gold ( int N ) {
  queue < int > q;
  q.push ( 1 );
  int cnt = 0;
  int t;
  while (!q.empty() ) {
    t = q.front();
    q.pop();
    if ( t <= N ) {
      cnt ++;
      q.push ( t * 10 );
      q.push ( t * 10 + 1 );
    }
  }
  return cnt;
}