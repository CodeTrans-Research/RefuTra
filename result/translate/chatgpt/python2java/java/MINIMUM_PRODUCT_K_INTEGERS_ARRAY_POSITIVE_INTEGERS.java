public int f_gold(int[] arr, int n, int k) {
    Queue<Integer> pq = new PriorityQueue<>();
    for (int i = 0; i < n; i++) {
        pq.add(arr[i]);
    }
    int count = 0;
    int ans = 1;
    while (!pq.isEmpty() && count < k) {
        ans += pq.poll();
        count++;
    }
    return ans;
}
