public static int f_gold ( int N ) {
        Deque<Integer> q = new ArrayDeque<>();
        q.addLast(1);
        int cnt = 0;
        while (!q.isEmpty()) {
            int t = q.removeFirst();
            if (t <= N) {
                cnt++;
                q.addLast(t * 10);
                q.addLast(t * 10 + 1);
            }
        }
        return cnt;
    }