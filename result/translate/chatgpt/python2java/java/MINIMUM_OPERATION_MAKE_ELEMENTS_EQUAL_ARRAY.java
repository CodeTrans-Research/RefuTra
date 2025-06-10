public static int f_gold(int[] arr, int n) {
    HashMap<Integer, Integer> Hash = new HashMap<>();
    for (int i = 0; i < n; i++) {
        Hash.put(arr[i], Hash.getOrDefault(arr[i], 0) + 1);
    }
    int max_count = 0;
    for (int i : Hash.keySet()) {
        if (max_count < Hash.get(i)) {
            max_count = Hash.get(i);
        }
    }
    return n - max_count;
}