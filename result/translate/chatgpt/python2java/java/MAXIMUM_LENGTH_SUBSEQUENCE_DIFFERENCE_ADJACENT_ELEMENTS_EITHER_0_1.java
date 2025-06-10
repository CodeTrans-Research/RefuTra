public static int f_gold(int[] arr, int n) {
    List<Integer> mls = new ArrayList<>();
    int max = 0;
    for (int i = 0; i < n; i++) {
        mls.add(1);
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (Math.abs(arr[i] - arr[j]) <= 1 && mls.get(i) < mls.get(j) + 1) {
                mls.set(i, mls.get(j) + 1);
            }
        }
    }
    for (int i = 0; i < n; i++) {
        if (max < mls.get(i)) {
            max = mls.get(i);
        }
    }
    return max;
}