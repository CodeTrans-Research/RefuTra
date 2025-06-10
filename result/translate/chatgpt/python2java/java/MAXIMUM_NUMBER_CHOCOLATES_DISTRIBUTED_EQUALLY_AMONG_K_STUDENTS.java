public static int f_gold(int[] arr, int n, int k) {
    Map<Integer, Integer> um = new HashMap<>();
    int curr_rem = 0, maxSum = 0;
    int[] sm = new int[n];
    sm[0] = arr[0];
    for (int i = 1; i < n; i++) {
        sm[i] = sm[i - 1] + arr[i];
    }
    for (int i = 0; i < n; i++) {
        curr_rem = sm[i] % k;
        if (curr_rem == 0 && maxSum < sm[i]) {
            maxSum = sm[i];
        } else if (!um.containsKey(curr_rem)) {
            um.put(curr_rem, i);
        } else if (maxSum < (sm[i] - sm[um.get(curr_rem)])) {
            maxSum = sm[i] - sm[um.get(curr_rem)];
        }
    }
    return maxSum / k;
}