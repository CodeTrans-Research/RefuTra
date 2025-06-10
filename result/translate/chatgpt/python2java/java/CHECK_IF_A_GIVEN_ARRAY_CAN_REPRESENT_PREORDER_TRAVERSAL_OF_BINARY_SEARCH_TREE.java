public boolean f_gold(int[] pre, int n) {
    List<Integer> s = new ArrayList<>();
    int root = Integer.MIN_VALUE;
    for (int i = 0; i < n; i++) {
        if (pre[i] < root) {
            return false;
        }
        while (!s.isEmpty() && s.get(s.size() - 1) < pre[i]) {
            root = s.remove(s.size() - 1);
        }
        s.add(pre[i]);
    }
    return true;
}