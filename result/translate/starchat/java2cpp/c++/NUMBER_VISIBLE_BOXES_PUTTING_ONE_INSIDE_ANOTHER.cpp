int f_gold ( int arr [ ] [ ] A, int n, int m ) {
    priority_queue<int, vector<int>, greater<int> > pq;
    for ( int i = 0; i < n; i++ ) pq.push(A[i][m - 1]);
    for ( int i = m - 2; i >= 0; i-- ) {
        A[0][i] = pq.top();
        pq.pop();
        for ( int j = 1; j < n; j++ ) {
            if ( A[j][i + 1] >= 2 * A[0][i] ) pq.push(A[j][i + 1]);
        }
    }
    int ans = 0;
    for ( int i = 0; i < n; i++ ) ans = max(ans, pq.size());
    return ans;
}