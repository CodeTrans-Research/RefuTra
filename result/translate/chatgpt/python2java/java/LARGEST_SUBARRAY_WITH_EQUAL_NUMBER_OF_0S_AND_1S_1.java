public static int f_gold(int[] arr, int n) {
    HashMap<Integer, Integer> hash_map = new HashMap<>();
    int curr_sum = 0;
    int max_len = 0;
    int ending_index = -1;
    for (int i = 0; i < n; i++) {
        if (arr[i] == 0) {
            arr[i] = -1;
        } else {
            arr[i] = 1;
        }
    }
    for (int i = 0; i < n; i++) {
        curr_sum = curr_sum + arr[i];
        if (curr_sum == 0) {
            max_len = i + 1;
            ending_index = i;
        }
        if (hash_map.containsKey(curr_sum + n)) {
            if (max_len < i - hash_map.get(curr_sum + n)) {
                max_len = i - hash_map.get(curr_sum + n);
                ending_index = i;
            }
        } else {
            hash_map.put(curr_sum + n, i);
        }
    }
    for (int i = 0; i < n; i++) {
        if (arr[i] == -1) {
            arr[i] = 0;
        } else {
            arr[i] = 1;
        }
    }
    System.out.print(ending_index - max_len + 1 + " ");
    System.out.print("to ");
    System.out.print(ending_index);
    return max_len;
}