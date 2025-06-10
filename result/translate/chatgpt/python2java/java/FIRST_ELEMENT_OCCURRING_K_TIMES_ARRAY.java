public static int f_gold(int arr[], int n, int k) {
    HashMap<Integer, Integer> countMap = new HashMap<>();
    for (int i = 0; i < n; i++) {
        if (countMap.containsKey(arr[i])) {
            countMap.put(arr[i], countMap.get(arr[i]) + 1);
        } else {
            countMap.put(arr[i], 1);
        }
    }
    for (int i = 0; i < n; i++) {
        if (countMap.get(arr[i]) == k) {
            return arr[i];
        }
    }
    return -1;
}