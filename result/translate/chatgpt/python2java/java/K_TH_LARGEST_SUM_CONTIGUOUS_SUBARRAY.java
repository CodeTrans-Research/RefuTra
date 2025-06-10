
public int f_gold(int[] arr, int n, int k) {
    List<Integer> sum = new ArrayList<>();
    sum.add(0);
    sum.add(arr[0]);
    for(int i=2; i<=n; i++) {
        sum.add(sum.get(i-1) + arr[i-1]);
    }
    Queue<Integer> Q = new PriorityQueue<>();
    for(int i=1; i<=n; i++) {
        for(int j=i; j<=n; j++) {
            int x = sum.get(j) - sum.get(i-1);
            if(Q.size() < k) {
                Q.add(x);
            } else {
                if(Q.peek() < x) {
                    Q.poll();
                    Q.add(x);
                }
            }
        }
    }
    return Q.peek();
}