public boolean f_gold(int[] arr, int n, int k) {
    Map<Integer, Integer> mp = new HashMap<>();
    for (int i = 0; i < n; i++) {
        mp.put(arr[i], mp.getOrDefault(arr[i], 0) + 1);
    }
    for (Map.Entry<Integer, Integer> entry : mp.entrySet()) {
        if (entry.getValue() > 2 * k) {
            return false;
        }
    }
    return true;
}