public static int f_gold(int [] arr, int n) {
    HashMap<Integer, Integer> um = new HashMap<>();
    int sum = 0;
    int maxLen = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] == 0) {
            sum += -1;
        } else {
            sum += 1;
        }
        if (sum == 1) {
            maxLen = i + 1;
        } else if (!um.containsKey(sum)) {
            um.put(sum, i);
        }
        if (um.containsKey(sum - 1)) {
            if (maxLen < (i - um.get(sum - 1))) {
                maxLen = i - um.get(sum - 1);
            }
        }
    }
    return maxLen;
}