public static int f_gold(int[] arr, int n) {
    int maxv = Arrays.stream(arr).max().getAsInt();
    int minv = Arrays.stream(arr).min().getAsInt();
    Map<Integer, Integer> mp = new HashMap<>();
    for (int i = minv; i <= maxv; i++) {
        mp.put(i, 0);
    }
    for (int i = 0; i < n; i++) {
        mp.put(arr[i], mp.get(arr[i]) + 1);
    }
    int res = 0;
    for (Map.Entry<Integer, Integer> entry : mp.entrySet()) {
        res = Math.max(res, entry.getValue());
    }
    return res;
}