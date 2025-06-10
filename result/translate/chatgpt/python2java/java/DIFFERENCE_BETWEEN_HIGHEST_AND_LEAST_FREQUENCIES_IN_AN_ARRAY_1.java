public int f_gold(int[] arr, int n) {
    HashMap<Integer, Integer> mp = new HashMap<>();

    for (int i = 0; i < n; i++) {
        mp.put(arr[i], mp.getOrDefault(arr[i], 0) + 1);
    }

    int max_count = 0;
    int min_count = n;

    for (int key : mp.keySet()) {
        int values = mp.get(key);
        max_count = Math.max(max_count, values);
        min_count = Math.min(min_count, values);
    }

    return max_count - min_count;
}
