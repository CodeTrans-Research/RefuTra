int f_gold ( int arr [ ], int n, int k ) {
    int sum[n+1];
    sum[0] = 0;
    sum[1] = arr[0];
    for(int i=2;i<=n;i++) sum[i] = sum[i-1] + arr[i-1];
    priority_queue<int, vector<int>, greater<int>> pq;
    for(int i=1;i<=n;i++){
        for(int j=i;j<=n;j++){
            int x = sum[j] - sum[i-1];
            if(pq.size() < k) pq.push(x);
            else{
                if(pq.top() < x) pq.pop();
                pq.push(x);
            }
        }
    }
    return pq.top();
}