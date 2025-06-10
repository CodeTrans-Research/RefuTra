int f_gold(int arr[], int n, int k) {
  priority_queue<int, vector<int>, greater<int>> pq;
  for (int i = 0; i < n; i++) pq.push(arr[i]);
  int count = 0, ans = 1;
  while (!pq.empty() && count < k) {
    ans += pq.top();
    pq.pop();
    count++;
  }
  return ans;
}