public static int f_gold(int[] A, int[] B, int n) {
    Map<Integer, Integer> hash = new HashMap<>();
    for (int i = 0; i < n; i++) {
        hash.put(A[i], hash.getOrDefault(A[i], 0) + 1);
        hash.put(B[i], hash.getOrDefault(B[i], 0) + 1);
    }
    int sum = 0;
    for (int x : hash.keySet()) {
        if (hash.get(x) == 1) {
            sum += x;
        }
    }
    return sum;
}