public static int f_gold(int[] arr, int n) {
    int min_prefix_sum = 0;
    int res = Integer.MIN_VALUE;
    List<Integer> prefix_sum = new ArrayList<>();
    prefix_sum.add(arr[0]);
    for (int i = 1; i < n; i++) {
        prefix_sum.add(prefix_sum.get(i - 1) + arr[i]);
    }
    for (int i = 0; i < n; i++) {
        res = Math.max(res, prefix_sum.get(i) - min_prefix_sum);
        min_prefix_sum = Math.min(min_prefix_sum, prefix_sum.get(i));
    }
    return res;
}