public static int f_gold(int N) {
    Queue<Integer> q = new LinkedList<>();
    q.offer(1);
    int cnt = 0;
    while (!q.isEmpty()) {
        int t = q.poll();
        if (t <= N) {
            cnt = cnt + 1;
            q.offer(t * 10);
            q.offer(t * 10 + 1);
        }
    }
    return cnt;
}
