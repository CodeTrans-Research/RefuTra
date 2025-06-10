public static int f_gold(int[] arr, int n) {
    Deque<Integer> q = new LinkedList<>();
    arr = Arrays.copyOf(arr, n);
    Arrays.sort(arr);
    q.add(arr[0]);
    for (int i = 1; i < n; i++) {
        int now = q.peekFirst();
        if (arr[i] >= 2 * now) {
            q.pollFirst();
        }
        q.add(arr[i]);
    }
    return q.size();
}